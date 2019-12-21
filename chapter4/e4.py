from typing import Tuple
import unittest

from .Graph import BinaryTree, BinaryNode


class BinaryTreeE4(BinaryTree):
    def is_balanced(self) -> bool:
        is_balanced, _ = self._is_balanced(self.root)
        return is_balanced

    def _is_balanced(self, root: BinaryNode) -> Tuple[bool, int]:
        left = root.left_child
        right = root.right_child
        if not (left or right):
            return True, 1

        if not (left and right):
            other = left or right
            is_balanced, height = self._is_balanced(other)
            return is_balanced and height == 1, height + 1

        is_left_balanced, left_height = self._is_balanced(left)
        is_right_balanced, right_height = self._is_balanced(right)

        is_balanced = (
            is_left_balanced
            and is_right_balanced
            and (abs(left_height - right_height) <= 1)
        )
        height = max(left_height, right_height) + 1
        return is_balanced, height


class Test(unittest.TestCase):
    def test_it(self):
        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)
        node4 = BinaryNode(4)
        node5 = BinaryNode(5)
        node6 = BinaryNode(6)
        node7 = BinaryNode(7)
        node1.left_child = node2
        node1.right_child = node3
        node2.left_child = node4
        node2.right_child = node5
        node3.left_child = node6
        node4.left_child = node7

        assert BinaryTreeE4(node1).is_balanced()


if __name__ == "__main__":
    unittest.main()
