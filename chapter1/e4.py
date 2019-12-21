import re
import sys


def is_permutation_of_palindrome(s: str) -> bool:
    """
    回文のアナグラムになっているか判定
    計算量は、文字数をs, 文字種をcとしている

    complexity: O(s+c)
    """

    # 各文字をキーとして、出現回数の奇遇を保持する
    # 奇数回出現した場合は1、偶数回出現した場合は0をセットする
    is_odd = {}

    for char in s:  # O(s)
        if re.match(r"\s", char):  # 1文字に対してのマッチなのでO(1)
            # 空白文字は無視する
            continue
        elif (char not in is_odd) or (is_odd[char] == 0):  # not in:O(1)
            # 文字が初めて出現orカウンターが0（これまでに偶数回出現している）なら、1をセットする
            is_odd[char] = 1
        elif is_odd[char] == 1:
            # カウンターが1（これまでに奇数回出現している）のときは、0をセットする
            is_odd[char] = 0
    # 奇数回出現する文字が1文字以下なら、並び替えによって回文は存在する
    # sum: O(c)
    return sum(is_odd.values()) < 2


if __name__ == "__main__":

    print(is_permutation_of_palindrome(sys.argv[1]))
