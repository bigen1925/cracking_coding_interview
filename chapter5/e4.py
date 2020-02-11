import unittest
from BitManipulator import BitManipulator

from typing import Tuple


def next_number(num: int) -> Tuple[int, int]:
    # previous
    # 0000111100011111
    #        ↑この1の桁iを見つける
    ones = 0
    zeros = 0
    num_tmp = num
    while num_tmp & 1 == 1:
        ones += 1
        num_tmp >>= 1
    while num_tmp & 1 == 0:
        zeros += 1
        num_tmp >>= 1
    i = ones + zeros + 1
    # i桁目を0にして、1を直前に並べる
    man = BitManipulator(num).clear_bit(i)
    for j in range(1, zeros):
        man.clear_bit(j)
    for j in range(zeros, i):
        man.set_bit(j)
    previous = man.value

    # next
    # 1111111000001111100000
    #            ↑この0の桁iを見つける
    ones = 0
    zeros = 0
    num_tmp = num
    while num_tmp & 1 == 0:
        zeros += 1
        num_tmp >>= 1
    while num_tmp & 1 == 1:
        ones += 1
        num_tmp >>= 1
    i = ones + zeros + 1
    # i 桁目を1にして、0を直前に並べる
    man = BitManipulator(num).set_bit(i)
    for j in range(1, ones):
        man.set_bit(j)
    for j in range(ones, i):
        man.clear_bit(j)
    next = man.value

    return previous, next


class TestMain(unittest.TestCase):
    def test_it(self):
        for num in [10, 22, 333, 444]:
            c = self.checker(num)
            n = next_number(num)
            assert c == n

    def checker(self, num):
        """
        無理やり答えを出すなにか
        """
        previous = num - 1
        count = BitManipulator(num).count_bit()
        while BitManipulator(previous).count_bit() != count:
            if previous < 1:
                raise

            previous -= 1

        next = num + 1
        while BitManipulator(next).count_bit() != count:
            if next > 10000:
                raise

            next += 1

        return previous, next


if __name__ == "__main__":
    unittest.main()
