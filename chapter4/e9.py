import unittest
from typing import List, Any
from copy import copy

from .Graph import BinaryTree, BinaryNode


class TreeE9(BinaryTree):
    def listing(self):
        return self._listing([self.root], [])

    def _listing(
        self, selectable: List[BinaryNode], prefix: List[Any]
    ) -> List[List[Any]]:
        if not selectable:
            return [prefix]

        ls = []

        for i, node in enumerate(selectable):
            next_selectable = copy(selectable)
            del next_selectable[i]
            if node.has_right_child:
                next_selectable.append(node.right_child)
            if node.has_left_child:
                next_selectable.append(node.left_child)

            next_prefix = copy(prefix)
            next_prefix.append(node.data)

            ls.extend(self._listing(next_selectable, next_prefix))

        return ls


class Test(unittest.TestCase):
    def test_it1(self):
        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)

        tree = TreeE9(node2.add_left(node1).add_right(node3))
        actual = tree.listing()

        expected = [[2, 3, 1], [2, 1, 3]]

        assert actual == expected

    def test_it2(self):
        # 3 --- 5
        #    |  |- 4
        #    |
        #    |- 2
        #       |- 1

        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)
        node4 = BinaryNode(4)
        node5 = BinaryNode(5)

        node3.add_left(node2).add_right(node5)
        node2.add_left(node1)
        node5.add_left(node4)

        tree = TreeE9(node3)
        actual = tree.listing()

        expected = [
            [3, 5, 2, 4, 1],
            [3, 5, 2, 1, 4],
            [3, 5, 4, 2, 1],
            [3, 2, 5, 1, 4],
            [3, 2, 5, 4, 1],
            [3, 2, 1, 5, 4],
        ]

        assert actual == expected


if __name__ == "__main__":
    unittest.main()
