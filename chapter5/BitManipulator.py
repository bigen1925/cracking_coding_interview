import unittest


class BitManipulator:
    def __init__(self, value):
        self._val = value

    def clear_bit(self, i):
        mask = ~(1 << (i - 1))
        self._val &= mask
        return self

    def set_bit(self, i):
        mask = 1 << (i - 1)
        self._val |= mask
        return self

    def count_bit(self) -> int:
        """
        2進数表記したときの1の数を数える
        """
        count = 0
        num = self.value
        while num != 0:
            if num & 1 == 1:
                count += 1

            num >>= 1

        return count

    @property
    def value(self):
        return self._val


class TestBitManipulator(unittest.TestCase):
    def test_set_bit(self):
        assert BitManipulator(0).set_bit(3).value == 0b100

    def test_clear_bit(self):
        assert BitManipulator(0b11111).clear_bit(3).value == 0b11011


if __name__ == "__main__":
    unittest.main()
