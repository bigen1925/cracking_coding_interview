from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, Optional
from unittest import mock


class Car:
    pass


class Space:
    id: Optional[int]
    is_empty: bool = True
    car: Optional[Car] = None
    entered_at: Optional[datetime] = None

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int):
        self.id = id


class Pricing(ABC):
    @staticmethod
    @abstractmethod
    def calculate(entered_at: datetime, leaved_at: datetime) -> int:
        pass


class UniformPricing(Pricing):
    @staticmethod
    def calculate(entered_at: datetime, leaved_at: datetime) -> int:
        """
        $5/h
        分は切り捨て（ただし、最小利用時間は1h）
        """
        used_time = leaved_at - entered_at
        hours = max(1, used_time // timedelta(hours=1))

        return 5 * hours


class ParkingException(Exception):
    pass


class ParkingLot:
    spaces: Dict[int, Optional[Space]]
    pricing: Pricing

    def __init__(self, capacity: int, pricing: Pricing):
        self.spaces = {i: Space(id=i) for i in range(capacity)}
        self.pricing = pricing

    def enter(self, car: Car) -> int:
        space = self.find_empty_space()
        if space is None:
            raise ParkingException("Empty Space does not exist.")

        now = datetime.now()

        space.is_empty = False
        space.car = car
        space.entered_at = now

        print(
            f"ParkingLot: Thank you for parking! We received your car at {now.strftime('%Y/%m/%d %H:%M.')}, "
            f"Your space_id is {space.id}."
        )

        return space.id

    # noinspection PyShadowingBuiltins
    def leave(self, id: int) -> Car:
        space = self.spaces.get(id)

        if space is None or space.is_empty:
            raise ParkingException(f"Your Car is not in that space (SpaceID: {id}).")

        now = datetime.now()

        # 料金を計算する
        price = self.pricing.calculate(entered_at=space.entered_at, leaved_at=now)
        # めんどくさいので料金は出力するだけにした
        print(
            f"ParkingLot: Thank you for using! We returned your cat at {now.strftime('%Y/%m/%d %H:%M.')}"
            f" and you will be charged ${price}."
        )

        car = space.car

        space.is_empty = True
        space.car = None
        space.entered_at = None

        return car

    def find_empty_space(self) -> Optional[Space]:
        for space in self.spaces.values():
            if space.is_empty:
                return space

        return None


if __name__ == '__main__':
    my_parking_lot = ParkingLot(capacity=100, pricing=UniformPricing())

    car = Car()

    now = datetime(2020, 1, 1)

    with mock.patch("__main__.datetime") as m:
        m.now.return_value = now
        space_id = my_parking_lot.enter(car)

    with mock.patch("__main__.datetime") as m:
        m.now.return_value = now + timedelta(hours=5, minutes=30)  # 5h30mは25$
        car_returned = my_parking_lot.leave(space_id)

    assert car == car_returned, "同じクルマ？"
