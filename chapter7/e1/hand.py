from abc import abstractmethod, ABC
from typing import Iterable, List

from chapter7.e1.card import Card, CardNumber


class Hand(ABC):
    """
    手札
    ・手札にカードを追加できる
    ・手札の点数を出すことができる
    """

    def __init__(self, cards: Iterable[Card] = ()):
        self.cards: List[Card] = []
        for card in cards:
            self.add_card(card)

    def add_card(self, card: Card) -> "Hand":
        self.cards.append(card)
        return self

    @property
    @abstractmethod
    def value(self):
        pass


class BlackJackHand(Hand):
    def __init__(self, cards: Iterable[Card] = ()):
        super().__init__(cards)

    @property
    def value(self) -> int:
        if len(self.cards) < 2:
            raise Exception("手札は2枚ないと点数が出ません")

        point = 0
        aces_included = False
        # エースはいったん1点で計算しておき、あとから11点にできるか考える
        for card in self.cards:
            if card.number >= CardNumber.TEN:
                # 絵札は全部10点
                point += 10
            else:
                point += card.number

            if aces_included is False and card.number is CardNumber.ACE:
                # エースがあったことを覚えておく
                aces_included = True

        if aces_included is True and point <= 10:
            # エースが手札に含まれていて、合計点が10点以下なら、エースは11点扱いとする
            point += 10

        if point > 21:
            return 0

        return point
