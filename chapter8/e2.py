from dataclasses import dataclass
from functools import cached_property
from random import random
from typing import List, Optional


class Field:
    width: int
    height: int
    p: float
    cells: List[List["Cell"]]

    def __init__(self, width, height, p=0.1):
        self.width = width
        self.height = height
        self.cells = [[Cell(x=x, y=y, disable=random() < p) for y in range(height)] for x in range(width)]

        self.start.disable = False
        self.goal.disable = False

        print(self.cells)

    def __getitem__(self, item):
        return self.cells[item]

    @property
    def start(self):
        return self[0][0]

    @cached_property
    def goal(self):
        return self[self.width - 1][self.height - 1]


@dataclass
class Cell:
    x: int
    y: int
    disable: bool

    def __sub__(self, other: "Cell"):
        if not isinstance(other, Cell):
            raise NotImplementedError("__sub__ of Cell")
        return (self.x - other.x) + (self.y - other.y)


def search_route(field: Field, start: Cell = None) -> Optional[List[Cell]]:
    if start is None:
        start = field.start
    goal = field.goal

    if start.disable:
        return None

    distance = goal - start
    if distance == 1:
        return [start, goal]
    else:
        if start.x + 1 < field.width:
            right_route = search_route(start=field[start.x + 1][start.y], field=field)
            if right_route:
                return [start] + right_route

        if start.y < field.height - 1:
            down_route = search_route(start=field[start.x][start.y + 1], field=field)
            if down_route:
                return [start] + down_route

    return None


if __name__ == '__main__':
    field = Field(width=3, height=3, p=0.2)

    route = search_route(field)

    print(route)
