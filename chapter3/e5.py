from .StackAndQueue import *
import unittest


class StackHelper:
    stack: Stack

    def __init__(self, stack: Stack) -> NoReturn:
        self.stack = stack

    def sort(self) -> "StackHelper":
        if self.stack.is_empty():
            return self

        tmp_stack = Stack()
        stack = self.stack
        self._transfer(stack, tmp_stack)

        # stackが空になるまで、繰り返しsortを行いながらtmp_stackへ移していく
        while not stack.is_empty():
            # stackの先頭のほうが、temp_stackの先頭より大きい場合、そのまま移しても降順ソートにならないので、
            # stackの先頭を取り出して保持しておき、tmp_stackを巻き戻していく
            if stack.peek() > tmp_stack.peek():
                # stackの先頭を保持
                item = stack.peek()
                stack.pop()
                # 保持したitemが降順でpushできる場所まで巻き戻す
                while not tmp_stack.is_empty() and item > tmp_stack.peek():
                    self._transfer(tmp_stack, stack)
                # 保持したitemをpushして、処理を続行
                tmp_stack.push(item)

            # temp_stackへ1つずつ移していく
            self._transfer(stack, tmp_stack)

        # tmp_stackがsortされたstackになっているので、stackと入れ替える
        self.stack = tmp_stack

        return self

    def get(self):
        return self.stack

    @staticmethod
    def _transfer(stack1: Stack, stack2: Stack):
        stack2.push(stack1.peek())
        stack1.pop()


class TestSortStack(unittest.TestCase):
    def test_initialize_and_stack(self):
        assert StackHelper(Stack([1, 2, 3])).get() == Stack([1, 2, 3])

    def test_min(self):
        s = Stack([3, 2, 1])
        assert StackHelper(s).sort().get() == Stack([3, 2, 1])
        s = Stack([3, 1, 2])
        assert StackHelper(s).sort().get() == Stack([3, 2, 1])
        s = Stack([2, 3, 1])
        assert StackHelper(s).sort().get() == Stack([3, 2, 1])
        s = Stack([2, 1, 3])
        assert StackHelper(s).sort().get() == Stack([3, 2, 1])
        s = Stack([1, 3, 2])
        assert StackHelper(s).sort().get() == Stack([3, 2, 1])
        s = Stack([1, 2, 3])
        assert StackHelper(s).sort().get() == Stack([3, 2, 1])


if __name__ == "__main__":
    unittest.main()
