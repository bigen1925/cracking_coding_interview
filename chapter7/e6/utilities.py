from abc import ABC, abstractmethod


class IdGenerator(ABC):
    @abstractmethod
    def generate(self) -> int:
        pass


class SequenceGenerator(IdGenerator):
    sequence: int

    def __init__(self, start: int = 1):
        self.sequence = start

    def generate(self) -> int:
        number = self.sequence
        self.sequence += 1
        return number
