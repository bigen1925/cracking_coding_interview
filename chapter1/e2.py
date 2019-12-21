def check_permutation(s1: str, s2: str) -> bool:
    """
    s1がs2の順列になっているかどうか確認する
    s1がs2の順列の時、逆にs2はs1の順列になっているので、片方向だけ調べれば十分
    全体でO(n)
    """

    # 文字列の長さが違う場合は順列ではあり得ない
    if len(s1) != len(s2):
        return False

    char_count = {}
    # s1に含まれる各文字の出現回数をカウントする
    # O(n)
    for char in s1:
        if char not in char_count:  # in dict: O(1)
            char_count[char] = 1
        else:
            char_count[char] += 1

    # s2に含まれる文字を1つずづチェックし、char_countの数を減らしていく
    # countが0なのにまた文字が出現したり、そもそも文字が存在しない場合はFalse
    # O(n)
    for char in s2:
        if (char not in char_count) or (char_count[char] == 0):  # O(1)
            return False
        else:
            char_count[char] -= 1

    return True
