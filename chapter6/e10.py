# 10days

# 1000個の瓶に0~999番の番号をつけるとする
#
# 1st day: 0~99 | 100~199 | 200~299 | ... | 900~999 の10グループにわけて試験する (100の位が0~9のグループ分け)
# 2nd day: 0~9, 100~109, ... | 10~19, 110~119, ... | 20~29, 120 ~ 129, ... | ... ... ... | 90~99, 190~199, ... | の10グループにわけて試験する (10の位が0~9のグループ分け)
# 3rd day: 1, 11, 21, ... , 991 | 2, 12, 22, ... , 992 | ... ... ... | 9, 19, 29, ... , 999 | の10グループにわけて試験する（1の位が0~9のグループ分け）
#
# 4~7th day: You can sleep deeply, zzz...
#
# 8th day: 100の位が0~9のどれか分かる
# 9th day: 10の位が0~9のどれか分かる
# 10th day: 1の位が0~9のどれか分かる <- 分からんときがある！
# 11th day: 1の位が0~9のどれか分かる
import unittest
from collections import deque
from functools import reduce
import random


class TestStripList(list):
    def sleep(self, day):
        for strip in self:
            strip.sleep(day)

    def get_positive_strip_indices(self):
        return [i for i, strip in enumerate(self) if strip.is_positive]


class TestStrip:
    def __init__(self):
        self.absorbed = deque()
        for i in range(7):
            self.absorbed.append([])
        self.is_positive = False

    def absorb(self, soda: "Soda"):
        self.absorbed[6].append(soda)

    def sleep(self, day: int):
        for i in range(day):
            self._sleep_one_day()

    def _sleep_one_day(self):
        sodas = self.absorbed.popleft()
        self.absorbed.append([])
        if self.is_positive:
            return

        for soda in sodas:
            if soda.is_poisoned:
                self.is_positive = True
                return


class Soda:
    def __repr__(self):
        return f"<{self.__class__} {id(self)}>"

    is_poisoned = False


class PoisonedSoda(Soda):
    is_poisoned = True


def main(poisoned_index=None):
    test_strips = TestStripList()
    for i in range(10):
        test_strips.append(TestStrip())

    soda_bottles = []
    for i in range(1000):
        soda_bottles.append(Soda())

    if poisoned_index is None:
        poisoned_index = random.randint(0, 999)
    soda_bottles[poisoned_index] = PoisonedSoda()

    # 1st day
    for i, soda in enumerate(soda_bottles):
        # 100の位がiのとき、strip_iにつける
        test_strips[i // 100].absorb(soda)
    test_strips.sleep(1)

    # 2nd day
    for i, soda in enumerate(soda_bottles):
        # 10の位がiのとき、strip_iにつける
        test_strips[(i // 10) % 10].absorb(soda)
    test_strips.sleep(1)

    # 3rd day
    for i, soda in enumerate(soda_bottles):
        # 1の位がiのとき、strip_iにつける
        test_strips[i % 10].absorb(soda)
    test_strips.sleep(1)

    # 4th day
    for i, soda in enumerate(soda_bottles):
        # 1の位がiのとき、strip_[i+1]につける
        test_strips[(i + 1) % 10].absorb(soda)
    test_strips.sleep(4)

    # 8th day
    positive_strips_1 = test_strips.get_positive_strip_indices()
    test_strips.sleep(1)

    # 9th day
    positive_strips_2 = test_strips.get_positive_strip_indices()
    test_strips.sleep(1)

    # 10th day
    positive_strips_3 = test_strips.get_positive_strip_indices()
    test_strips.sleep(1)

    # 11th day
    positive_strips_4 = test_strips.get_positive_strip_indices()

    # Result
    # 初日の結果は100の位を決める
    hundreds_place = positive_strips_1[0]

    # 二日目の結果は10の位を決める
    if len(positive_strips_2) != len(positive_strips_1):
        # 二日目にpositiveな試験紙が増えた場合は、増えたやつが10の位を表す
        tens_place = reduce(
            lambda x, y: x if x not in positive_strips_1 else y, positive_strips_2
        )
    elif len(positive_strips_2) == 1:
        # 1つの試験紙だけがpositiveの場合は、それが10の位を表す
        tens_place = positive_strips_2[0]
    else:
        raise Exception()

    # 三日目の結果は1の位を決める（決められないこともある）
    if len(positive_strips_2) != len(positive_strips_3):
        # 三日目にpositiveな試験紙が増えた場合は、増えたやつが1の位を表す
        ones_place = reduce(
            lambda x, y: x if x not in positive_strips_2 else y, positive_strips_3
        )
    elif len(positive_strips_3) == 1:
        # 1つの試験紙だけがpositiveの場合は、それが1の位を表す
        ones_place = positive_strips_3[0]
    elif len(positive_strips_3) == 2:
        # 二日目に2つの試験紙がpositiveで、三日目も2つの試験紙がpositiveの場合、決められない
        ones_place = None
    else:
        raise Exception()

    # 1の位が決まらなかった場合は4日目の結果も見て、1の位を決める
    if ones_place is None:
        if len(positive_strips_3) != len(positive_strips_4):
            # 4日目にpositiveな試験紙が増えた場合は、(増えたやつ-1)が1の位を表す
            ones_place = (
                reduce(
                    lambda x, y: x if x not in positive_strips_3 else y,
                    positive_strips_4,
                )
                - 1
            )
        elif len(positive_strips_4) == 2:
            # 4日目でもpositiveな試験紙が2つしかない場合、試験紙が並んでいるはずなので1つめが1の位を決める
            ones_place = positive_strips_4[0]

    # 答え
    poisoned_soda_number = hundreds_place * 100 + tens_place * 10 + ones_place

    return poisoned_soda_number


class Test(unittest.TestCase):
    def test(self):
        poison_indices = [0, 11, 111, 123, 122, 112, 999]
        for poison_index in poison_indices:
            assert poison_index == main(poison_index)


if __name__ == "__main__":
    unittest.main()
