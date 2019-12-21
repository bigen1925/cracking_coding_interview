from .LinkedList import SinglyLinkedList, SinglyLinkedNode
import unittest


class SinglyLinkedListE8(SinglyLinkedList):
    def has_circulation(self):
        """
        循環があるかどうか
        """
        follower = self.get_head()
        runner = self.get_head()

        while True:
            # runnerは2歩進む。終端についたら循環なし
            if not runner.has_next():
                return False
            runner = runner.next()
            if not runner.has_next():
                return False
            runner = runner.next()
            # followerは1歩進む。
            follower = follower.next()

            # 何故かrunnerがfollowerに追いついたら循環あり
            if follower is runner:
                return True

    def append_node(self, node):
        self.get_tail().set_next(node)
        return self


class TestSinglyLinkedListE8(unittest.TestCase):
    def test_has_circulation(self):
        node = SinglyLinkedNode(3)

        ls = (
            SinglyLinkedListE8([1, 2])
            .append_node(node)
            .append(4)
            .append(5)
            .append_node(node)
        )

        assert ls.has_circulation() is True

    def test_has_circulation2(self):

        ls = SinglyLinkedListE8([1, 2, 3, 4, 5])

        assert ls.has_circulation() is False


if __name__ == "__main__":
    unittest.main()
