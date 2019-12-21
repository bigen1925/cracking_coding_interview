from typing import List
import unittest

from Graph import BinaryTree, BinaryNode


def make_binary_search_tree(ls: List[int]) -> BinaryTree:
    """
    与えられたリストを半分に分割して、
    左側を最小木、右側も最小木で生成すれば、全体として最小木になる

    深さ優先で木を生成するので、空間計算量はO(log(num_nodes))
    1回のコールあたり1ノードを確定させるので、時間計算量はO(log(num_nodes))
    """
    num = len(ls)
    tree = BinaryTree()

    if num == 0:
        return tree

    if num == 1:
        tree.root = BinaryNode(ls[0])
        return tree

    if num == 2:
        tree.root = BinaryNode(ls[0])
        tree.root.right_child = BinaryNode(ls[1])
        return tree

    top = BinaryNode([num // 2])

    left_tree = make_binary_search_tree(ls[: (num // 2 - 1)])
    right_tree = make_binary_search_tree(ls[: (num // 2 + 1)])

    top.left_child = left_tree.root
    top.right_child = right_tree.root

    return tree


class TestMakeBinarySearchTree:
    def test_make_binary_search_tree1(self):
        ls = [1]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 1
        assert tree.root.left_child is None
        assert tree.root.right_child is None

    def test_make_binary_search_tree2(self):
        ls = [1, 2]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 1
        assert tree.root.left_child is None
        assert tree.root.right_child == 2

    def test_make_binary_search_tree3(self):
        ls = [1, 2, 3]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 2
        assert tree.root.left_child == 1
        assert tree.root.left_child.left_child is None
        assert tree.root.left_child.right_child is None
        assert tree.root.right_child == 3
        assert tree.root.right_child.left_child is None
        assert tree.root.right_child.right_child is None

    def test_make_binary_search_tree4(self):
        ls = [1, 2, 3, 4]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 3
        assert tree.root.left_child == 1
        assert tree.root.left_child.left_child is None
        assert tree.root.left_child.right_child == 2
        assert tree.root.left_child.right_child.left_child is None
        assert tree.root.left_child.right_child.right_child is None
        assert tree.root.right_child == 4
        assert tree.root.right_child.left_child is None
        assert tree.root.right_child.right_child is None

    def test_make_binary_search_tree5(self):
        ls = [1, 2, 3, 4, 5]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 3
        assert tree.root.left_child == 1
        assert tree.root.left_child.left_child is None
        assert tree.root.left_child.right_child == 2
        assert tree.root.left_child.right_child.left_child is None
        assert tree.root.left_child.right_child.right_child is None
        assert tree.root.right_child == 4
        assert tree.root.right_child.left_child is None
        assert tree.root.right_child.right_child == 5
        assert tree.root.right_child.right_child.left_child is None
        assert tree.root.right_child.right_child.right_child is None

    def test_make_binary_search_tree6(self):
        ls = [1, 2, 3, 4, 5, 6]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 4
        assert tree.root.left_child == 3
        assert tree.root.left_child.left_child == 1
        assert tree.root.left_child.left_child.left_child is None
        assert tree.root.left_child.left_child.right_child is None
        assert tree.root.left_child.right_child == 2
        assert tree.root.left_child.right_child.left_child is None
        assert tree.root.left_child.right_child.right_child is None
        assert tree.root.right_child == 5
        assert tree.root.right_child.left_child is None
        assert tree.root.right_child.right_child == 6
        assert tree.root.right_child.right_child.left_child is None
        assert tree.root.right_child.right_child.right_child is None

    def test_make_binary_search_tree7(self):
        ls = [1, 2, 3, 4, 5, 6, 7]
        tree = make_binary_search_tree(ls)

        assert tree.root.data == 4
        assert tree.root.left_child == 3
        assert tree.root.left_child.left_child == 1
        assert tree.root.left_child.left_child.left_child is None
        assert tree.root.left_child.left_child.right_child is None
        assert tree.root.left_child.right_child == 2
        assert tree.root.left_child.right_child.left_child is None
        assert tree.root.left_child.right_child.right_child is None
        assert tree.root.right_child == 6
        assert tree.root.right_child.left_child == 5
        assert tree.root.right_child.left_child.left_child is None
        assert tree.root.right_child.left_child.right_child is None
        assert tree.root.right_child.right_child == 7
        assert tree.root.right_child.right_child.left_child is None
        assert tree.root.right_child.right_child.right_child is None


if __name__ == "__main__":
    unittest.main()
