import unittest


def squeeze_right(n: int, m: int = 1, bit: int = 1):
    n = n << m

    if bit == 0:
        return n

    for i in range(m):
        n = n | (1 << i)

    return n


def insertion(n: int, m: int, i: int, j: int):
    # 1111111000001111 みたいなのを作る
    mask_bits = ~(squeeze_right(0, j - i + 1, 1) << i)

    # nのj~i桁目を0にする
    output = n & mask_bits

    # mをi桁ずらして入れる
    output = output & (m << i)

    return output


class TestMain(unittest.TestCase):
    def test_it(self):
        n = 0b11110000000000000000000000000000
        m = 0b00000000000000000000000001110011
        i = 3
        j = 7
        expected = 0b11110000000000000000001110011000

        assert insertion(n, m, i, j) == expected


if __name__ == "__main__":
    unittest.main()
