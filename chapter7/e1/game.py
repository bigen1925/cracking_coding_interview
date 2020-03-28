from abc import ABC, abstractmethod
from typing import Iterable, List, Optional

from chapter7.e1.card import Suit, CardNumber, Card
from chapter7.e1.deck import Deck
from chapter7.e1.hand import BlackJackHand


class Player:
    """
    ゲームのプレイヤー
    ここでは、
    ・手札を持っている
    ・手札を評価することができる
    ことを前提としている
    """

    def __init__(self):
        self.hand: Optional[Hand] = None

    def evaluate_hand(self):
        return self.hand.value

    def set_hand(self, hand: "Hand") -> "Player":
        self.hand = hand
        return self

    def draw(self, deck: Deck) -> "Player":
        self.hand.add_card(deck.eject())
        return self


class Game(ABC):
    """
    それぞれのゲームを表す
    ここでは、
    ・トランプを使う
    ・初期山札がある
    ・プレイヤーを追加できる
    ことを最低限のルールとしている
    """

    def __init__(self, players: Iterable[Player] = ()):
        self.players: List[Player] = list(players)

    @staticmethod
    @abstractmethod
    def get_initial_deck() -> Deck:
        pass

    def add_player(self, player: Player) -> "Game":
        self.players.append(player)
        return self


class BlackJack(Game):
    """
    ブラックジャック
    """

    @staticmethod
    def get_initial_deck() -> Deck:
        # 4スート13枚の52枚を初期山札とする
        cards = [
            Card(suit, number)
            for suit in Suit.__members__.values()
            for number in CardNumber.__members__.values()
        ]
        return Deck(cards)

    def add_player(self, player: Player) -> "BlackJack":
        player.set_hand(BlackJackHand())

        return self
