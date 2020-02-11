import unittest
from BitManipulator import BitManipulator


def conversion(n: int, m: int) -> int:
    return BitManipulator(xor(n, m)).count_bit()


def xor(n: int, m: int) -> int:
    return n & ~m | ~n & m


class TestMain(unittest.TestCase):
    def test_it(self):
        assert conversion(29, 15) == 2


if __name__ == "__main__":
    unittest.main()
