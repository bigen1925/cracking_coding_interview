import unittest
from copy import copy

from .Graph import BinaryTree, BinaryNode
from typing import Dict


Counts = Dict[int, int]


class PathCounts:
    inc_root: Counts
    non_inc_root: Counts

    def __init__(self, inc_root: Counts, non_inc_root: Counts):
        self.inc_root = inc_root
        self.non_inc_root = non_inc_root


class TreeE12(BinaryTree):
    def paths_with_sum(self, sum: int) -> int:
        counts = self.count_paths_group_by_sum(self.root)
        return counts[sum]

    def count_paths_group_by_sum(self, root: BinaryNode) -> Counts:
        rec_count = self._rec_count_paths_group_by_sum(root)

        return self.merge_counts(rec_count.inc_root, rec_count.non_inc_root)

    def _rec_count_paths_group_by_sum(self, node: BinaryNode) -> PathCounts:
        if not node.has_left_child and not node.has_right_child:
            return PathCounts({node.data: 1}, {})

        if node.has_left_child:
            left_counts = self._rec_count_paths_group_by_sum(node.left_child)
            non_inc_root_from_left = self.merge_counts(
                left_counts.inc_root, left_counts.non_inc_root
            )

            inc_root_from_left = {}
            for key, value in left_counts.inc_root.items():
                inc_root_from_left[key + node.data] = value

        if node.has_right_child:
            right_counts = self._rec_count_paths_group_by_sum(node.right_child)
            non_inc_root_from_right = self.merge_counts(
                right_counts.inc_root, right_counts.non_inc_root
            )

            inc_root_from_right = {}
            for key, value in right_counts.inc_root.items():
                inc_root_from_right[key + node.data] = value

        if not node.has_right_child:
            non_inc_root = non_inc_root_from_left
            inc_root = inc_root_from_left
        elif not node.has_left_child:
            non_inc_root = non_inc_root_from_right
            inc_root = inc_root_from_right
        else:
            non_inc_root = self.merge_counts(
                non_inc_root_from_left, non_inc_root_from_right
            )
            inc_root = self.merge_counts(inc_root_from_left, inc_root_from_right)

        inc_root = self.merge_counts(inc_root, {node.data: 1})

        return PathCounts(inc_root, non_inc_root)

    @staticmethod
    def merge_counts(counts1: Counts, counts2: Counts) -> Counts:
        counts = copy(counts1)
        for key, value in counts2.items():
            if key in counts:
                counts[key] += value
            else:
                counts[key] = value

        return counts


class Test(unittest.TestCase):
    def test_it1(self):
        """
        1 - 2 - 6
          |   - 7
          - 3 - 4
              + 5
        """
        node1 = BinaryNode(1)
        node2 = BinaryNode(2)
        node3 = BinaryNode(3)
        node4 = BinaryNode(4)
        node5 = BinaryNode(5)
        node6 = BinaryNode(6)
        node7 = BinaryNode(7)

        node1.add_left(node2).add_right(node3)
        node2.add_left(node6).add_right(node7)
        node3.add_left(node4).add_right(node5)

        # 合計値ごとにパスの個数を全て出せる
        assert TreeE12(node1).count_paths_group_by_sum(node1) == {
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 1,
            6: 1,
            7: 2,
            8: 3,
            9: 3,
            10: 1,
        }
        # 合計値を1つ指定しても当然合っている
        assert TreeE12(node1).paths_with_sum(8) == 3


if __name__ == "__main__":
    unittest.main()
