def multiple(m, n):
    mm = m
    result = 0
    while n != 0:
        if n & 1:
            result += mm

        n >>= 1
        mm += mm

    return result


if __name__ == '__main__':
    assert multiple(3, 5) == 15
    assert multiple(2, 9) == 18
    assert multiple(12, 12) == 144

