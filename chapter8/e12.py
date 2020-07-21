from typing import List


class Queen(tuple):
    @property
    def row(self):
        return self[0]

    @property
    def col(self):
        return self[1]


def solve(queens: List[Queen] = None):
    if queens is None:
        queens = []

    if len(queens) == 8:
        return queens

    row = len(queens)
    cols = set(range(0, 8))

    for col in cols:
        if is_positionable(row, col, queens):
            new_queens = queens + [Queen([row, col])]
            if result := solve(new_queens):
                return result

    return None


def is_positionable(row, col, queens: List[Queen]) -> bool:
    for queen in queens:
        if col == queen.col:
            return False

        if row + col == queen.row + queen.col:
            return False

        if row - col == queen.row - queen.col:
            return False

    return True


if __name__ == "__main__":
    queens = solve()
    print(queens)

    board = [["-" for col in range(1, 9)] for row in range(1, 9)]

    for queen in queens:
        board[queen.row][queen.col] = "*"

    print("\n".join([" ".join(row) for row in board]))
