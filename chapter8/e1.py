import unittest


def steps(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        # 1+1 or 2
        return 2
    elif n == 3:
        # 1+1+1 or 1+2 or 2+1 or 3
        return 4
    else:
        return steps(n - 3) + steps(n - 2) + steps(n - 1)


class Test(unittest.TestCase):
    def test(self):
        assert steps(1) == 1
        assert steps(2) == 2
        assert steps(3) == 4
        assert steps(4) == 7
        assert steps(5) == 13


if __name__ == '__main__':
    unittest.main()
