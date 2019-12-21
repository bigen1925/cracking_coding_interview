from LinkedList import SinglyLinkedList
import unittest


class SinglyLinkedListE1(SinglyLinkedList):
    def unique(self) -> "SinglyLinkedListE1":
        if not self.has_head():
            return self
        values = []
        node = self.get_head()

        while node.has_next():
            values.append(node.value())
            while node.has_next() and node.next().value() in values:
                self.delete_next_node(node)

            if node.has_next():
                node = node.next()
        return self


class TestLinkListE1(unittest.TestCase):
    def testUniqueToEmpty(self):
        assert SinglyLinkedListE1().unique() == SinglyLinkedListE1()

    def testUnique(self):
        assert SinglyLinkedListE1([0, 0, 1, 1, 2, 2]).unique() == SinglyLinkedListE1(
            [0, 1, 2]
        )


if __name__ == "__main__":
    unittest.main()
