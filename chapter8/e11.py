from typing import List


def solve(n: int, coins: List[int] = None):
    if coins is None:
        coins = [25, 10, 5, 1]

    if n == 0 or coins == [1]:
        return 1

    count = 0
    coin = coins[0]

    while n >= 0:
        count += solve(n, coins[1:])
        n -= coin

    return count


if __name__ == "__main__":
    assert solve(1) == 1
    assert solve(4) == 1
    assert solve(5) == 2
    assert solve(9) == 2
    assert solve(10) == 4
    assert solve(15) == 6
    assert solve(20) == 9
    assert solve(25) == 13
    assert solve(50) == 49
