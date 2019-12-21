from typing import Dict, Any, List
import unittest

from .Graph import BinaryTree, BinaryNode


class BinaryTreeE3(BinaryTree):
    def make_lists_of_depth(
        self,
        node: BinaryNode = None,
        depth: int = 1,
        lists: Dict[int, List[Any]] = None,
    ) -> Dict[List[Any]]:
        if node is None:
            node = self.root

        if lists is None:
            lists = []

        lists[depth].append(node.data)

        if node.left_child is not None:
            lists = self.make_lists_of_depth(
                node=node.left_child, depth=depth + 1, lists=lists
            )

        if node.right_child is not None:
            lists = self.make_lists_of_depth(
                node=node.right_child, depth=depth + 1, lists=lists
            )

        return lists


class TestE3(unittest.TestCase):
    def test_e3_1(self):
        node = BinaryNode(1)

        assert BinaryTreeE3(node).make_lists_of_depth() == {1: [1]}

    def test_e3_2(self):
        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)

        node1.left_child = node2
        node1.right_child = node3

        assert BinaryTreeE3(node1).make_lists_of_depth() == {1: [1], 2: [2, 3]}

    def test_e3_3(self):
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
        node3.right_child = node7

        assert BinaryTreeE3(node1).make_lists_of_depth() == {
            1: [1],
            2: [2, 3],
            3: [4, 5, 6, 7],
        }


if __name__ == "__main__":
    unittest.main()
