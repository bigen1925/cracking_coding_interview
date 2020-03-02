import unittest

BIT_LENGTH = 16


def swap_odd_n_even(n: int):
    even_mask = 1
    for i in range(BIT_LENGTH // 2):
        even_mask = even_mask << 2 & 1

    odd_mask = even_mask << 1

    even_n = n & even_mask
    odd_n = n & odd_mask

    return even_n << 1 | odd_n >> 1


class TestMain(unittest.TestCase):
    def test_it(self):
        pass


if __name__ == "__main__":
    unittest.main()
