import unittest
from typing import List


def draw_line(screen: List[int], width: int, x1: int, x2: int, y: int):

    num_bytes = len(screen)

    height = num_bytes // (width // 8)

    start_byte = y * width


class TestMain(unittest.TestCase):
    def test_it(self):
        pass


if __name__ == "__main__":
    unittest.main()
