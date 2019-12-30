import unittest
from typing import Optional

from .Graph import BinaryTree, BinaryNode


class InOrderSuccessor:
    def __init__(self, tree: BinaryTree):
        self._root = tree.root
        self.current: Optional[BinaryNode] = None

    def __next__(self):
        self.current = self.next(self.current)
        if self.current is None:
            raise StopIteration
        return self.current

    def next(self, node: Optional[BinaryNode]) -> Optional[BinaryNode]:
        # 一番最初はルートノードの左端を返す
        if node is None:
            return self.get_left_terminal(self._root)

        # 右に木があれば、右の木の左端を返す
        if node.has_right_child:
            return self.get_left_terminal(node.right_child)

        # 最初の右親を返す
        return self.get_right_ancestor(node)

    @staticmethod
    def get_left_terminal(node: BinaryNode) -> BinaryNode:
        while node.has_left_child:
            node = node.left_child

        return node

    @staticmethod
    def get_right_ancestor(node: BinaryNode) -> Optional[BinaryNode]:
        while True:
            if not node.has_parent:
                return None

            if node.is_left_child:
                return node.parent

            node = node.parent


class BinaryTreeE6(BinaryTree):
    def __iter__(self):
        return InOrderSuccessor(self)


class Test(unittest.TestCase):
    def test_it(self):
        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)
        node4 = BinaryNode(4)
        node5 = BinaryNode(5)
        node6 = BinaryNode(6)
        node7 = BinaryNode(7)

        node1.add_left(node2).add_right(node3)
        node2.add_left(node4).add_right(node5)
        node3.add_left(node6).add_right(node7)

        tree = BinaryTreeE6(node1)
        assert [node for node in tree] == [
            node4,
            node2,
            node5,
            node1,
            node6,
            node3,
            node7,
        ]


if __name__ == "__main__":
    unittest.main()
