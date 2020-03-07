from abc import abstractmethod, ABC
from random import shuffle
from typing import List


class Weighable(ABC):
    @property
    @abstractmethod
    def weight(self) -> float:
        pass


class Medicine(Weighable, ABC):
    _weight: int

    @property
    def weight(self) -> float:
        return self.__class__._weight


class Medicine10(Medicine):
    _weight = 1.0


class Medicine11(Medicine):
    _weight = 1.1


class WeighableContainer(Weighable, list):
    def __init__(self, *args, **kwargs):
        self._weight: float = 0

        super().__init__(*args, **kwargs)

    def append(self, item: Weighable) -> None:
        if not isinstance(item, Weighable):
            raise ValueError("Only Weighable can be appended.")

        self._weight += item.weight
        return super().append(item)

    @property
    def weight(self) -> float:
        return self._weight


class Bottle:
    def __init__(self, content_class: type):
        self.content_class = content_class

    def pick(self):
        return self.content_class()


class OnceScale:
    def __init__(self):
        self.is_used = False

    def weigh(self, item: Weighable) -> float:
        if self.is_used is True:
            raise ValueError("this scale can weigh only once.")

        self.is_used = True

        return item.weight


def solve(bottles: List[Bottle]):
    container = WeighableContainer()

    for i, bottle in enumerate(bottles):
        for j in range(i):
            container.append(bottle.pick())

    scale = OnceScale()
    weight = scale.weigh(container)

    error = weight - 190.0

    return round(error * 10.0)


if __name__ == "__main__":
    bottles = [Bottle(Medicine11)]
    for i in range(19):
        bottles.append(Bottle(Medicine10))
    shuffle(bottles)

    expected = 999
    for i, bottle in enumerate(bottles):
        if isinstance(bottle.pick(), Medicine11):
            expected = i

    actual = solve(bottles)

    assert actual == expected
