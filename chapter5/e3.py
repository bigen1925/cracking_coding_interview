import unittest


def flip_bit_to_win(num: int):
    max_continuation = 0
    previous_continuation = 0
    current_continuation = 0

    while num != 0:
        num = num >> 1

        if (num & 1) == 0:
            continuation = previous_continuation + current_continuation + 1
            max_continuation = max(max_continuation, continuation)
            previous_continuation = current_continuation
            current_continuation = 0
        else:
            current_continuation += 1

    return max_continuation


class TestMain:
    def test_it(self):
        assert flip_bit_to_win(0b110110111) == 6
        assert flip_bit_to_win(0b110101110) == 5
        assert flip_bit_to_win(0b110111111) == 9
        assert flip_bit_to_win(0b101010101) == 3


if __name__ == "__main__":
    unittest.main()
