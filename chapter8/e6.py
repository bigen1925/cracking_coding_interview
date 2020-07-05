from collections import deque
from sys import argv
from typing import List


class Disc(int):
    pass


class Tower(deque):
    _T = Disc

    def __init__(self, n: int):
        super().__init__()

        for i in range(n):
            disc = Disc(n - i)
            self.append(disc)

    def append(self, x: _T) -> None:
        if self and self[-1] <= x:
            raise Exception("自分より大きい円盤の上にしか置けません")

        super().append(x)


class HanoiSolver:
    step: int
    towers: List[Tower]

    def __init__(self, n: int):
        self.step = 0
        self.towers = [Tower(n), Tower(0), Tower(0)]

    def __repr__(self):
        s = "---------------\n"
        s += f"tower0: {''.join([str(disc) for disc in self.towers[0]])}\n"
        s += f"tower1: {''.join([str(disc) for disc in self.towers[1]])}\n"
        s += f"tower2: {''.join([str(disc) for disc in self.towers[2]])}\n"
        s += "---------------\n"

        return s

    def solve(self) -> None:
        print("始まるよ〜")
        print(self)

        # tower0からtower2へn枚の円盤を動かす
        n = len(self.towers[0])
        self._move(n, 0, 2)

        print("やったね！")

    def _move(self, n: int, fr: int, to: int) -> None:
        """
        tower[fr]からtower[to]へn枚の円盤を動かす
        """
        if n == 1:
            # 手数を進める
            self.step += 1
            # fromからtoへ1枚だけ動かす
            disc = self.towers[fr].pop()
            self.towers[to].append(disc)
            # 結果を出力する
            print(f"{self.step}手目: tower{fr} から tower{to} へ '{disc}' を移動しました")
            print(self)
            return

        # n-1枚の円盤を一時的に避難させる塔（frでもtoでもないところ）
        tmp = 3 - fr - to
        # まずfrからtmpへn-1枚動かす
        self._move(n-1, fr, tmp)
        # frからtoへ1枚動かす
        self._move(1, fr, to)
        # tmpからtoへn-1枚動かす
        self._move(n-1, tmp, to)


if __name__ == '__main__':
    n = int(argv[1])
    HanoiSolver(n).solve()
