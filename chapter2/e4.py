from LinkedList import SinglyLinkedList
import unittest


class SinglyLinkedListE4(SinglyLinkedList):
    def partition(self, threshold):
        """
        先頭から順に、threshold未満の値が並ぶ区画をサーチし、区画ごと先頭へ付け替えていく
        O(n)
        ex) xxABxxCDExxF -> ABxxxxCDExxxF -> CDEABxxxxxxxF -> FCDEABxxxxxxx

        :param threshold: partitionするしきい値
        :return:
        """
        search_head = self._get_initial_search_head(threshold)
        # threshold未満の区画がなくなるまでループ
        while True:

            # threshold未満の区画の直前のノードまで進める
            search_head = self._update_search_head(search_head, threshold)
            # 区画がもうなければpartition済みなので、ループを抜けて終了する
            if not search_head:
                break

            # threshold未満の区画の最後のノードを取得する
            runner = search_head.next()
            while runner.has_next() and runner.next().value() < threshold:
                runner = runner.next()

            # 区画ごと先頭につけかえる
            new_head = search_head.next()  # 区画の先頭
            if runner.has_next():  # サーチヘッドのnextを、区画のnextにつけかえる
                search_head.set_next(runner.next())
            else:
                search_head.delete_next()  # 区画に後続がなければ、サーチヘッドのnextはdeleteする
            runner.set_next(self.get_head())  # 区画の後続は、現在のリストの先頭ノードにする
            self.set_head(new_head)  # リストの先頭を区画の先頭にする

        return self

    def _get_initial_search_head(self, threshold):
        search_head = self.get_head()
        while search_head.next().value() < threshold:
            search_head = search_head.next()
        while search_head.next().value() >= threshold:
            search_head = search_head.next()
        return search_head

    @staticmethod
    def _update_search_head(search_head, threshold):
        ended = False
        while True:
            if not search_head.has_next():
                ended = True
                break
            elif search_head.next().value() < threshold:
                break
            else:
                search_head = search_head.next()

        return search_head if not ended else None


class TestSinglyLinkedListE4(unittest.TestCase):
    def test_partition(self):
        ls = SinglyLinkedListE4([3, 5, 8, 5, 10, 2, 1])
        ls.partition(5)

        assert ls == SinglyLinkedListE4([2, 1, 3, 5, 8, 5, 10])


if __name__ == "__main__":
    unittest.main()
