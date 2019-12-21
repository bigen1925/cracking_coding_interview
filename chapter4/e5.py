import unittest
from typing import Tuple, Any

from .Graph import BinaryTree, BinaryNode


class BinaryTreeE5(BinaryTree):
    def is_search_tree(self):
        is_search, _, _ = self._is_search_tree(self.root)
        return is_search

    def _is_search_tree(self, node: BinaryNode) -> Tuple[bool, Any, Any]:
        left = node.left_child
        right = node.right_child
        if left is None and right is None:
            return True, node.data, node.data

        if left is None:
            is_right_search, right_min, right_max = self._is_search_tree(right)
            if is_right_search is False or right_min <= node.data:
                return False, None, None
            return True, node.data, right_max

        if right is None:
            is_left_search, left_min, left_max = self._is_search_tree(left)
            if is_left_search is False or node.data < left_max:
                return False, None, None
            return True, left_min, node.data

        is_left_search, left_min, left_max = self._is_search_tree(left)
        if is_left_search is False or node.data < left_max:
            return False, None, None

        is_right_search, right_min, right_max = self._is_search_tree(right)
        if is_right_search is False or right_min <= node.data:
            return False, None, None

        return True, left_min, right_max


class Test(unittest.TestCase):
    def test_it(self):
        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)
        node4 = BinaryNode(4)
        node5 = BinaryNode(5)
        node6 = BinaryNode(6)
        node7 = BinaryNode(7)
        node4.left_child = node2
        node2.left_child = node1
        node2.right_child = node3
        node4.right_child = node6
        node6.left_child = node5
        node6.right_child = node7

        assert BinaryTreeE5(node1).is_search_tree() is True


if __name__ == "__main__":
    unittest.main()
