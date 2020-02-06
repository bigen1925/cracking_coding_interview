import unittest


def flip_bit_to_win(num: int):
    # 1桁目を取得
    first_bit = num & 1
    # 連続する2つの塊の合計長さの最大値（区切りの0も長さに含む）
    max_continuation = 0
    # 1つ前の塊の長さ
    previous_continuation = 0
    # 現在探索中の塊の長さ
    current_continuation = first_bit

    while num != 0:
        # 右シフトして次の桁を見る
        num = num >> 1

        first_bit = num & 1
        if first_bit == 0:
            # 1桁目が0のとき、直近2連続の塊の長さを計算し、最大長と比較して更新する
            continuation = previous_continuation + current_continuation + 1
            max_continuation = max(max_continuation, continuation)
            previous_continuation = current_continuation
            current_continuation = 0
        else:
            # 1桁目が1のときは粛々と計算を続行
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
