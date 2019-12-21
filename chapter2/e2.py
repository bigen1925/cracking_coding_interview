from LinkedList import SinglyLinkedList
from typing import Any
import unittest


class SinglyLinkedListE2(SinglyLinkedList):
    def kth_to_last(self, k: int) -> Any:
        if k < 1:
            raise IndexError("kth_to_last() is invalid. k should be positive.")

        try:
            node = self.get_head()
            runner = node
            for i in range(k - 1):
                runner = runner.next()
        except LookupError:
            raise IndexError(
                "kth_to_last() is invalid. k is too long than length of list."
            )

        while runner.has_next():
            node = node.next()
            runner = runner.next()

        return node.value()


class TestLinkListE2(unittest.TestCase):
    def testKthToEmpty(self):
        with self.assertRaises(IndexError):
            SinglyLinkedListE2().kth_to_last(1)

    def testKthTooShort(self):
        with self.assertRaises(IndexError):
            SinglyLinkedListE2([0, 1]).kth_to_last(3)

    def testKth(self):
        assert SinglyLinkedListE2([0, 1, 2, 3, 4, 5]).kth_to_last(4) == 2


if __name__ == "__main__":
    unittest.main()
