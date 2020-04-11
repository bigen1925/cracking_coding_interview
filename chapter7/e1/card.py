from enum import Enum, IntEnum


class Suit(Enum):
    SPADE = 1
    CLUB = 2
    DIAMOND = 3
    HEART = 4


class CardNumber(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    def __init__(self, suit: Suit, number: CardNumber):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.suit_name} {self.number}>"

    @property
    def suit_name(self):
        if self.suit is Suit.SPADE:
            suit_name = "SPADE"
        elif self.suit is Suit.CLUB:
            suit_name = "CLUB"
        elif self.suit is Suit.DIAMOND:
            suit_name = "DIAMOND"
        elif self.suit is Suit.HEART:
            suit_name = "HEART"
        else:
            raise ValueError("Unknown Suit")

        return suit_name
