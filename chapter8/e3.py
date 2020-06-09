import unittest
from random import sample
from time import time
from typing import List


def search_magic_index(target: List[int], start_index: int = None, end_index: int = None):
    # 検索区間が与えられてない場合は、全区間を検索する
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(target) - 1

    # 検索区間の始端と終端の値がindexと一致していれば、区間全体がmagic indexになっている
    if target[start_index] == start_index and target[end_index] == end_index:
        return target[start_index:end_index + 1]

    # 検索区間のindexが、始端と終端の値の内側に入っている場合は、区間の一部がmagic indexになっているので、
    # 前半分と後ろ半分に分割して再度検索する
    if target[start_index] <= start_index and end_index <= target[end_index]:
        # 始端と終端の中間のindexを取得
        half = (end_index + start_index) // 2
        # 前半分の検索結果を取得
        first = search_magic_index(
            target,
            start_index=start_index,
            end_index=half,
        )
        # 後ろ半分の検索結果を取得
        second = search_magic_index(
            target,
            start_index=half + 1,
            end_index=end_index
        )
        # 結果を結合して返す
        return first + second

    # 検索区間のindexが始端と終端の内側に入らない場合は、magic indexは存在しない
    return []


class Test(unittest.TestCase):
    def test(self):
        assert search_magic_index([0, 1, 2]) == [0, 1, 2]
        assert search_magic_index([-1, 1, 3]) == [1]
        assert search_magic_index([-1, 1, 2]) == [1, 2]
        assert search_magic_index([1, 2, 3]) == []
        assert search_magic_index([-1, 0, 1]) == []

    def testTime(self):
        # 実行時間の比較

        # サンプルの配列を生成
        targets = [
            {"sample": s, "target": sorted(sample(range(-s // 100, s + (s // 100)), k=s))}
            for s in [100, 1000, 10000, 100000, 1000000]
        ]

        # 解法の実行時間
        print(f"\n========my method=======:")
        for target in targets:
            start = time()
            result = search_magic_index(target["target"])
            exec_time = time() - start
            print(f"sample: {target['sample']}, time:{exec_time}, result: {result}")

        # 総当り法の実行時間
        print(f"\n========brute force method=======:")
        for target in targets:
            start = time()
            result = [v for i, v in enumerate(target["target"]) if i == v]
            exec_time = time() - start
            print(f"sample: {target['sample']}, time:{exec_time}, result: {result}")


if __name__ == '__main__':
    unittest.main()
