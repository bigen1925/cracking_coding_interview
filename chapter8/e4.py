from itertools import combinations


def power_set(ls: list, n: int = None):
    if n is None:
        n = len(ls)
    if n == 0:
        return set()

    ret = power_set(ls, n - 1)

    for t in combinations(ls, n):
        ret.add(t)

    return ret


if __name__ == '__main__':
    print(power_set([1, 2, 3]))
    assert power_set([1, 2, 3]) == {(1, 2, 3), (1, 2), (1, 3), (2, 3), (1, ), (2, ), (3, )}
