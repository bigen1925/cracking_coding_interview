import operator
import itertools

OPS = {
    "&": operator.and_,
    "|": operator.or_,
    "^": operator.xor,
}


def countEval(s: str, b: bool):
    if len(s) == 1:
        return 1 if int(s) == b else 0

    count = 0
    for i, op_string in enumerate(s[1::2]):
        pos = 2 * i + 1
        for b1, b2 in itertools.product((True, False), repeat=2):
            if OPS[op_string](b1, b2) == b:
                count += countEval(s[:pos], b1) * countEval(s[pos + 1:], b2)

    # if op == "&":
    #     if b is True:
    #         count += countEval(s[:pos], True) * countEval(s[pos:], True)
    #     elif b is False:
    #         count += countEval(s[:2 * i + 1], True) * countEval(s[2 * i + 2:], False)
    #         count += countEval(s[:2 * i + 1], False) * countEval(s[2 * i + 2:], True)
    #         count += countEval(s[:2 * i + 1], False) * countEval(s[2 * i + 2:], False)
    # elif op == "|":
    #     if b is True:
    #         count += countEval(s[:2 * i + 1], True) * countEval(s[2 * i + 2:], True)
    #         count += countEval(s[:2 * i + 1], True) * countEval(s[2 * i + 2:], False)
    #         count += countEval(s[:2 * i + 1], False) * countEval(s[2 * i + 2:], True)
    #     elif b is False:
    #         count += countEval(s[:2 * i + 1], False) * countEval(s[2 * i + 2:], False)
    # elif op == "^":
    #     if b is True:
    #         count += countEval(s[:2 * i + 1], True) * countEval(s[2 * i + 2:], False)
    #         count += countEval(s[:2 * i + 1], False) * countEval(s[2 * i + 2:], True)
    #     elif b is False:
    #         count += countEval(s[:2 * i + 1], True) * countEval(s[2 * i + 2:], True)
    #         count += countEval(s[:2 * i + 1], False) * countEval(s[2 * i + 2:], False)

    return count


if __name__ == '__main__':
    assert countEval("1^0|0|1", False) == 2
    assert countEval("0&0&0&1^1|0", True) == 10
