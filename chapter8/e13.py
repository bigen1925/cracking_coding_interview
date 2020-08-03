from typing import Iterable, Optional


class Box:
    def __init__(self, wi, hi, di):
        self.wi = wi
        self.hi = hi
        self.di = di

    def __lt__(self, other: Optional["Box"]):
        return other is None or (self.wi < other.wi and self.hi < other.hi and self.di < other.di)


def solve(boxes: Iterable[Box], top_box: Box = None, cur_hi: int = 0):
    highest = cur_hi
    for box in boxes:
        if box < top_box:
            highest = max(highest, solve((b for b in boxes if b is not box), box, cur_hi + box.hi))
    return highest


if __name__ == '__main__':
    boxes = [Box(1, 1, 1)]
    assert solve(boxes) == 1

    boxes = [Box(1, 1, 1), Box(2, 2, 2)]
    assert solve(boxes) == 3

    boxes = [Box(3, 1, 2), Box(1, 3, 3), Box(2, 3, 5)]
    assert solve(boxes) == 3

    boxes = [Box(3, 1, 2), Box(1, 3, 3), Box(2, 4, 5)]
    assert solve(boxes) == 7
