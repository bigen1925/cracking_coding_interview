from .StackAndQueue import *
import unittest


class StackWithLength(Stack):
    length: int = 0
    max_len: int

    def __init__(self, iterable=(), max_len: int = 0):
        self.max_len = max_len
        super().__init__(iterable)

    def pop(self) -> "StackWithLength":
        super().pop()
        self.length -= 1
        return self

    def push(self, item) -> "StackWithLength":
        if self.is_full():
            raise LookupError("push() is invalid. Stack is full.")

        super().push(item)
        self.length += 1
        return self

    def is_full(self) -> bool:
        return self.length >= self.max_len


class StackOfStacks(Stack):
    max_len: int

    def __init__(self, iterable=(), max_len: int = 0):
        self.max_len = max_len
        super().__init__(iterable)

    def pop(self) -> "StackOfStacks":
        if self.is_empty():
            raise LookupError("pop() is invalid. StackOfStacks is empty.")

        # 先頭のスタックから要素を削除し、空になっていたら、スタックごと取り除く
        if super().peek().pop().is_empty():
            super().pop()
            return self

    def push(self, item) -> "StackOfStacks":
        if self.is_empty() or super().peek().is_full():
            # スタックがないか、先頭のスタックがいっぱいなら、新しいスタックを作成して追加する
            stack = StackWithLength(max_len=self.max_len)
            super().push(stack)
        else:
            stack = super().peek()

        stack.push(item)
        return self

    def peek(self):
        return super().peek().peek()

    def pop_at(self, index):
        tmp_stacks = Stack()

        for i in range(index - 1):
            tmp_stacks.push(super().peek())
            super().pop()

        self.pop()

        while not tmp_stacks.is_empty():
            super().push(tmp_stacks.peek())
            tmp_stacks.pop()


class TestStackOfStacks(unittest.TestCase):
    def test_initialize(self):
        StackOfStacks(max_len=11)
        StackOfStacks([1, 2, 3], max_len=1)

    def test_is_empty(self):
        assert StackOfStacks(max_len=10).is_empty() is True
        assert StackOfStacks([1], max_len=10).is_empty() is False
        assert StackOfStacks([1], max_len=10).pop().is_empty() is True

    def test_peek(self):
        assert StackOfStacks([1], max_len=1).peek() == 1
        assert StackOfStacks([1, 2], max_len=1).peek() == 2
        with self.assertRaises(LookupError):
            StackOfStacks(max_len=1).peek()

    def test_pop(self):
        s = StackOfStacks([1, 2], max_len=1)
        assert s.pop() == StackOfStacks([1], max_len=1)
        assert s.pop() == StackOfStacks(max_len=1)
        with self.assertRaises(LookupError):
            s.pop()

    def test_pop_at1(self):
        s1 = StackOfStacks([1, 2, 3, 4, 5], max_len=2)
        s2 = StackOfStacks([1, 2, 3, 4], max_len=2)
        s1.pop_at(1)
        assert s1 == s2

    def test_pop_at2(self):
        s1 = StackOfStacks([1, 2, 3, 4, 5], max_len=2)
        s2 = StackOfStacks([1, 2, 3, 4, 5], max_len=2)
        s2.top.next.data.pop()
        s1.pop_at(2)
        assert s1 == s2

    def test_pop_at3(self):
        s1 = StackOfStacks([1, 2, 3, 4, 5], max_len=2)
        s2 = StackOfStacks([1, 2, 3, 4, 5], max_len=2)
        s2.top.next.next.data.pop()
        s1.pop_at(3)
        assert s1 == s2


if __name__ == "__main__":
    unittest.main()
