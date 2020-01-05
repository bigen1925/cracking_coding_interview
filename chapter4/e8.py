import unittest
from typing import List
from copy import deepcopy

from .Graph import BinaryTree, BinaryNode


class TreeE8(BinaryTree):
    @classmethod
    def find_common_ancestor(cls, node1: BinaryNode, node2: BinaryNode) -> BinaryNode:
        # 探索ヘッド
        pointer1 = node1
        pointer2 = node2
        # ノードの深さを取得
        height1 = cls.get_depth(node1)
        height2 = cls.get_depth(node2)
        # 探索ヘッドの深さを揃える
        if height1 < height2:
            for i in range(height2 - height1):
                pointer2 = pointer2.parent
        elif height2 < height1:
            for i in range(height1 - height2):
                pointer1 = pointer1.parent
        # 探す
        while True:
            # 発見
            if pointer1 is pointer2:
                return pointer1
            # 遡れなくなったらエラー
            if not pointer1.has_parent or not pointer2.has_parent:
                raise LookupError("共通祖先は存在しません")

            pointer1 = pointer1.parent
            pointer2 = pointer2.parent

    @classmethod
    def get_depth(cls, node: BinaryNode) -> int:
        pointer = node
        depth = 1
        while pointer.has_parent:
            depth += 1
            pointer = pointer.parent

        return depth


class Test(unittest.TestCase):
    def test_it(self):
        node1 = BinaryNode()
        node2 = BinaryNode()
        node3 = BinaryNode()
        node4 = BinaryNode()
        node5 = BinaryNode()
        node6 = BinaryNode()
        node7 = BinaryNode()

        node1.add_left(node2).add_right(node3)
        node2.add_left(node4).add_right(node5)
        node3.add_left(node6).add_right(node7)

        assert TreeE8.find_common_ancestor(node1, node2) is node1
        assert TreeE8.find_common_ancestor(node2, node3) is node1
        assert TreeE8.find_common_ancestor(node4, node5) is node2
        assert TreeE8.find_common_ancestor(node4, node3) is node1
        assert TreeE8.find_common_ancestor(node6, node7) is node3
        assert TreeE8.find_common_ancestor(node4, node7) is node1


if __name__ == "__main__":
    unittest.main()
