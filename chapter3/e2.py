import unittest
from .StackAndQueue import *


class StackNodeHasMin(Node):
    min = 0

    def __init__(self, data, next, min):
        super().__init__(data, next)
        self.min = min


class StackE2(Stack):
    def push(self, item) -> "StackE2":
        # 一個手前のやつのmin（これまでの最小値）と比べて、自分の方が小さければ自分の値を自分のminとする
        # そうでなければ、一個手前のやつのminが自分のmin
        # O(1)でいける
        if self.is_empty() or item < self.top.min:
            min = item
        else:
            min = self.top.min

        self.top = StackNodeHasMin(item, self.top, min)  # O(1)
        return self

    def min(self):
        self.check_empty()
        return self.top.min


class TestStackE2(unittest.TestCase):
    def test_min(self):
        assert StackE2([1, 2, 3]).min() == 1
        assert StackE2([2, 1, 3]).min() == 1
        assert StackE2([2, 3, 1]).min() == 1
        assert StackE2([1, 2, 3]).pop().min() == 1
        assert StackE2([3, 2, 1]).pop().min() == 2
        assert StackE2([3, 2, 1]).pop().pop().min() == 3

        with self.assertRaises(LookupError):
            StackE2().min()


if __name__ == "__main__":
    unittest.main()
