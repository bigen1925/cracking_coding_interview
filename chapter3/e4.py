from .StackAndQueue import *
import unittest


class StackDeQueue:
    forward_stack: Stack
    reversed_stack: Stack

    def __init__(self, iterable=()) -> NoReturn:
        self.forward_stack = Stack()
        self.reversed_stack = Stack()
        for item in iterable:
            self.add(item)

    def __eq__(self, other: "StackDeQueue") -> bool:
        return (
            self.forward_stack == other.forward_stack
            and self.reversed_stack == other.reversed_stack
        )

    def _reverse_if_needed(self) -> NoReturn:
        """
        reversed_stackが空っぽのときだけ、forward_stackをひっくり返す
        """
        if self.reversed_stack.is_empty() and not self.forward_stack.is_empty():
            # Reverse stack
            while not self.forward_stack.is_empty():
                self.reversed_stack.push(self.forward_stack.peek())
                self.forward_stack.pop()

    def add(self, item) -> "StackDeQueue":
        self.forward_stack.push(item)
        return self

    def peek(self):
        self._reverse_if_needed()
        return self.reversed_stack.peek()

    def remove(self) -> "StackDeQueue":
        self._reverse_if_needed()
        self.reversed_stack.pop()
        return self

    def is_empty(self) -> bool:
        return self.reversed_stack.is_empty() and self.forward_stack.is_empty()


class TestStackDeQueue(unittest.TestCase):
    def test_reverse(self):
        q = StackDeQueue([1, 2])
        assert q.forward_stack == Stack([1, 2])
        assert q.reversed_stack == Stack()
        assert q.peek() == 1
        assert q.forward_stack == Stack()
        assert q.reversed_stack == Stack([2, 1])
        q.add(3).add(4)
        assert q.forward_stack == Stack([3, 4])
        assert q.reversed_stack == Stack([2, 1])
        assert q.peek() == 1
        assert q.forward_stack == Stack([3, 4])
        assert q.reversed_stack == Stack([2, 1])
        q.remove()
        assert q.forward_stack == Stack([3, 4])
        assert q.reversed_stack == Stack([2])
        q.remove()
        assert q.forward_stack == Stack([3, 4])
        assert q.reversed_stack == Stack([])
        q.remove()
        assert q.forward_stack == Stack([])
        assert q.reversed_stack == Stack([4])

    def test_is_empty(self):
        assert StackDeQueue().is_empty() is True
        assert StackDeQueue([1]).is_empty() is False
        assert StackDeQueue([1]).remove().is_empty() is True
        assert StackDeQueue([1, 2]).remove().is_empty() is False
        assert StackDeQueue([1, 2]).remove().remove().is_empty() is True


if __name__ == "__main__":
    unittest.main()
