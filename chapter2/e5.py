from .LinkedList import SinglyLinkedList
import unittest


class SinglyLinkedListE5(SinglyLinkedList):
    def reverse_digit_sum(self, another):
        node1 = self.get_head()
        node2 = another.get_head()
        summed_list = self.__class__()
        carry = 0
        zero_node = self._create_node(0, None)

        while True:
            sum = node1.value() + node2.value() + carry
            ones_place = sum % 10
            carry = sum // 10
            summed_list.append(ones_place)

            if not node1.has_next() and not node2.has_next() and not carry:
                break

            node1 = node1.next() if node1.has_next() else zero_node
            node2 = node2.next() if node2.has_next() else zero_node

        return summed_list

    def forward_digit_sum(self, another):
        int1 = self.to_integer()
        int2 = another.to_integer()

        return self.make_with_integer(int1 + int2)

    def to_integer(self):
        node = self.get_head()
        integer = node.value()
        while node.has_next():
            node = node.next()
            integer = integer * 10 + node.value()
        return integer

    @classmethod
    def make_with_integer(cls, input):
        integer = input
        ls = cls()
        while integer:
            ls.append_head(integer % 10)
            integer = integer // 10

        return ls


class TestSinglyLinkedListE5(unittest.TestCase):
    def test_reverse_digit_sum(self):
        ls1 = SinglyLinkedListE5([7, 1, 6])
        ls2 = SinglyLinkedListE5([5, 9, 2])
        summed = ls1.reverse_digit_sum(ls2)
        assert summed == SinglyLinkedListE5([2, 1, 9])

    def test_reverse_digit_sum2(self):
        ls1 = SinglyLinkedListE5([9, 9])
        ls2 = SinglyLinkedListE5([1, 0, 9])
        summed = ls1.reverse_digit_sum(ls2)
        assert summed == SinglyLinkedListE5([0, 0, 0, 1])

    def test_forward_digit_sum(self):
        ls1 = SinglyLinkedListE5([6, 1, 7])
        ls2 = SinglyLinkedListE5([2, 9, 5])
        summed = ls1.forward_digit_sum(ls2)
        assert summed == SinglyLinkedListE5([9, 1, 2])

    def test_forward_digit_sum2(self):
        ls1 = SinglyLinkedListE5([9, 9])
        ls2 = SinglyLinkedListE5([9, 0, 1])
        summed = ls1.forward_digit_sum(ls2)
        assert summed == SinglyLinkedListE5([1, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
