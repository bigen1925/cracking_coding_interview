from .LinkedList import SinglyLinkedList, SinglyLinkedNode
import unittest


class SinglyLinkedListE7(SinglyLinkedList):
    def has_intersection(self, another):
        """
        共通ノードがあるかどうかを判定する
        ある点でノードが共通するとき、そのノード移行も全く同じになるはずなので、最後のノードだけ調べれば良い
        """
        return self.get_tail() is another.get_tail()

    def append_node(self, node):
        return self.get_tail().set_next(node)

    def get_tail(self):
        """
        append_nodeするとheadがずれることが判明したのでoverride
        """
        node = self.get_head()
        while node.has_next():
            node = node.next()
        return node


class TestSinglyLinkedListE7(unittest.TestCase):
    def test_has_intersection(self):
        ls1 = SinglyLinkedListE7([1, 2])
        ls2 = SinglyLinkedListE7([1, 2])
        assert ls1.has_intersection(ls2) is False

    def test_has_intersection2(self):
        node = SinglyLinkedNode(2)
        ls1 = SinglyLinkedListE7([1]).append_node(node)
        ls2 = SinglyLinkedListE7([1]).append_node(node)
        assert ls1.has_intersection(ls2) is True

    def test_has_intersection3(self):
        node = SinglyLinkedNode(2)
        ls1 = SinglyLinkedListE7([1]).append_node(node).append(3)
        ls2 = SinglyLinkedListE7([1]).append_node(node).append(4)
        assert ls1 == SinglyLinkedListE7([1, 2, 3, 4])
        assert ls2 == SinglyLinkedListE7([1, 2, 3, 4])
        assert ls1.has_intersection(ls2) is True


if __name__ == "__main__":
    unittest.main()
