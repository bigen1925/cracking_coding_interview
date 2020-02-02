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
        """
        上にあるノードから追加されているはずなので、上にあるノードからリストに加えていくと、
        木を導くリストが作れる

        selectable 次に選択するノード候補
        prefix これまで選択してきたノード
        """

        # 次に選択するノードがなければそのまま返す
        if not selectable:
            return [prefix]

        ls = []

        # 次のノード候補を順に選択し、それぞれのノードを選択した時の全ての選択肢をリストアップしてくっつけていく
        for i, node in enumerate(selectable):
            # selectableからノードを一つ選んで候補から削除し、その子ノードを次のノード候補に追加する
            next_selectable = copy(selectable)
            del next_selectable[i]
            if node.has_right_child:
                next_selectable.append(node.right_child)
            if node.has_left_child:
                next_selectable.append(node.left_child)

            # 選んだノードをprefixに追加する
            next_prefix = copy(prefix)
            next_prefix.append(node.data)

            # このノードを選択した時のリストを全て出し、くっつける
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
