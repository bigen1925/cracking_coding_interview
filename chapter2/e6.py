from .LinkedList import DoublyLinkedList
import unittest


class SinglyLinkedListE6(DoublyLinkedList):
    def is_palindrome(self):
        forward_node = self.get_head()
        reverse_node = self.get_tail()

        while forward_node is not reverse_node and (
            not forward_node.has_prev() or forward_node.prev() is not reverse_node
        ):
            if forward_node.value() != reverse_node.value():
                return False
            forward_node = forward_node.next()
            reverse_node = reverse_node.prev()

        return True


class TestSinglyLinkedListE6(unittest.TestCase):
    def test_is_palindrome(self):
        assert SinglyLinkedListE6([1, 2, 3, 2, 1]).is_palindrome() is True

    def test_is_palindrome2(self):
        assert SinglyLinkedListE6([1, 2, 3, 3, 2, 1]).is_palindrome() is True

    def test_is_palindrome3(self):
        assert SinglyLinkedListE6([1, 2, 3, 1, 2]).is_palindrome() is False

    def test_is_palindrome4(self):
        assert SinglyLinkedListE6([1, 2, 4, 3, 2, 1]).is_palindrome() is False


if __name__ == "__main__":
    unittest.main()
