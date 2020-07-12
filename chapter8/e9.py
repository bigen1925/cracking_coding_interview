import unittest
from typing import Set, Dict


# noinspection DuplicatedCode
class Solver:
    call_count: int

    def __init__(self):
        self.call_count = 0

    def valid_combinations(self, n: int) -> Set[str]:
        if n == 0:
            return {""}
        self.call_count += 1

        combinations = set()
        for i in range(n):
            first = self.valid_combinations(i)
            second = self.valid_combinations(n - 1 - i)

            for f in first:
                for s in second:
                    combinations.add("(" + f + ")" + s)

        self.call_count += 1
        return combinations


# noinspection DuplicatedCode
class CacheSolver:
    call_count: int
    cache: Dict[int, Set[str]]

    def __init__(self):
        self.call_count = 0
        self.cache = {}

    def valid_combinations(self, n: int) -> Set[str]:
        # 既に計算済みであればキャッシュした値を使う
        if n in self.cache:
            return self.cache[n]

        if n == 0:
            return {""}
        self.call_count += 1

        combinations = set()
        for i in range(n):
            first = self.valid_combinations(i)
            second = self.valid_combinations(n - 1 - i)

            for f in first:
                for s in second:
                    combinations.add("(" + f + ")" + s)

        # キャッシュに保存する
        self.cache[n] = combinations
        return combinations


class Test(unittest.TestCase):
    def test_output(self):
        assert Solver().valid_combinations(0) == {""}
        assert Solver().valid_combinations(1) == {"()"}
        assert Solver().valid_combinations(2) == {"()()", "(())"}
        assert Solver().valid_combinations(3) == {"()()()", "(())()", "()(())", "(()())", "((()))"}
        assert Solver().valid_combinations(4) == {
            "()()()()", "()(())()", "()()(())", "()(()())", "()((()))", "(())()()",
            "(())(())", "(()())()", "((()))()", "(()()())", "((())())", "(()(()))",
            "((()()))", "(((())))"
        }

        assert CacheSolver().valid_combinations(0) == {""}
        assert CacheSolver().valid_combinations(1) == {"()"}
        assert CacheSolver().valid_combinations(2) == {"()()", "(())"}
        assert CacheSolver().valid_combinations(3) == {"()()()", "(())()", "()(())", "(()())", "((()))"}
        assert CacheSolver().valid_combinations(4) == {
            "()()()()", "()(())()", "()()(())", "()(()())", "()((()))", "(())()()",
            "(())(())", "(()())()", "((()))()", "(()()())", "((())())", "(()(()))",
            "((()()))", "(((())))"
        }

    def test_call_count(self):
        for n in range(10):
            print(f":::: n={n} ::::")
            solver1 = Solver()
            solver1.valid_combinations(n)
            solver2 = CacheSolver()
            solver2.valid_combinations(n)
            print(f"normal = {solver1.call_count}, cache = {solver2.call_count}")


if __name__ == '__main__':
    unittest.main()
