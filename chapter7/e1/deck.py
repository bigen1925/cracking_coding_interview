from random import shuffle
from typing import Iterable, List

from chapter7.e1.card import Card


class Deck:
    def __init__(self, cards: Iterable[Card] = None, shuffling=True):
        if cards is None:
            cards = []
        self.cards: List[Card] = list(cards)

        if shuffling is True:
            self.shuffle()

    def eject(self):
        return self.cards.pop()

    def shuffle(self) -> "Deck":
        shuffle(self.cards)
        return self
