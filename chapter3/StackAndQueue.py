import unittest
from typing import NoReturn, Any, Optional


class Node:
    data = None
    next: Optional["Node"] = None

    def __init__(self, data=None, next: "Node" = None, *args, **kwargs) -> NoReturn:
        self.data = data
        self.next = next

    def __eq__(self, other: "Node") -> bool:
        return self.data == other.data

    def has_next(self) -> bool:
        return self.next is not None


class Stack:
    top: Optional[Node] = None

    def __init__(self, iterable=()) -> NoReturn:
        for item in iterable:
            self.push(item)

    def __eq__(self, other: "Stack") -> bool:
        if self.is_empty() != other.is_empty():
            # length are different
            return False
        if self.is_empty() and other.is_empty():
            return True

        node1 = self.top
        node2 = other.top
        while True:
            if node1 != node2:
                return False

            if node1.has_next() != node2.has_next():
                # length are different
                return False
            if not node1.has_next() and not node2.has_next():
                return True

            node1 = node1.next
            node2 = node2.next

    def pop(self) -> "Stack":
        self.check_empty()
        if self.top.has_next():
            self.top = self.top.next
        else:
            self.top = None
        return self

    def push(self, item) -> "Stack":
        self.top = Node(item, self.top)
        return self

    def peek(self) -> Any:
        self.check_empty()
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

    def check_empty(self) -> NoReturn:
        if self.is_empty():
            raise LookupError("Stack is empty.")


class Queue:
    first: Optional[Node] = None
    last: Optional[Node] = None

    def __init__(self, iterable=()):
        for item in iterable:
            self.add(item)

    def __eq__(self, other: "Queue") -> bool:
        if self.is_empty() != other.is_empty():
            return False
        elif self.is_empty() and other.is_empty():
            return True

        node1 = self.first
        node2 = other.first
        while True:
            if node1 != node2:
                return False

            if node1.has_next() != node2.has_next():
                return False

            if not node1.has_next() and not node2.has_next():
                return True

            node1 = node1.next
            node2 = node2.next

    def add(self, item) -> "Queue":
        node = Node(item, None)
        if self.last is None:
            self.first = node
        else:
            self.last.next = node
        self.last = node
        return self

    def remove(self) -> "Queue":
        self.check_empty()
        if self.first.has_next():
            self.first = self.first.next
        else:
            self.first = self.last = None
        return self

    def peek(self):
        self.check_empty()
        return self.first.data

    def is_empty(self) -> bool:
        return self.first is None

    def check_empty(self) -> NoReturn:
        if self.is_empty():
            raise LookupError("Queue is empty.")


class TestStack(unittest.TestCase):
    def test_initialize(self):
        Stack()
        Stack([1, 2, 3])

    def test_eq(self):
        assert Stack() == Stack()
        assert Stack([1, 2, 3]) == Stack([1, 2, 3])
        assert Stack([1, 2, 3]) == Stack((1, 2, 3))

    def test_is_empty(self):
        assert Stack().is_empty() is True
        assert Stack([1]).is_empty() is False

    def test_peek(self):
        assert Stack([1]).peek() == 1
        assert Stack([1, 2]).peek() == 2
        with self.assertRaises(LookupError):
            Stack().peek()

    def test_pop(self):
        s = Stack([1, 2])
        assert s.pop() == Stack([1])
        assert s.pop() == Stack()
        with self.assertRaises(LookupError):
            s.pop()

    def test_push(self):
        s = Stack()
        assert s.push(1) == Stack([1])
        assert s.push(2) == Stack([1, 2])
        assert s.push(3).push(4) == Stack([1, 2, 3, 4])


class TestQueue(unittest.TestCase):
    def test_initialize(self):
        Queue()
        Queue([1, 2, 3])

    def test_eq(self):
        assert Queue() == Queue()
        assert Queue([1, 2, 3]) == Queue([1, 2, 3])
        assert Queue([1, 2, 3]) == Queue((1, 2, 3))

    def test_is_empty(self):
        assert Queue().is_empty() is True
        assert Queue([1]).is_empty() is False

    def test_peek(self):
        assert Queue([1]).peek() == 1
        assert Queue([1, 2]).peek() == 1
        with self.assertRaises(LookupError):
            Queue().peek()

    def test_remove(self):
        s = Queue([1, 2])
        assert s.remove() == Queue([2])
        assert s.remove() == Queue()
        with self.assertRaises(LookupError):
            s.remove()

    def test_add(self):
        s = Queue()
        assert s.add(1) == Queue([1])
        assert s.add(2) == Queue([1, 2])
        assert s.add(3).add(4) == Queue([1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
