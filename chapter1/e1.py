def check1(s: str) -> bool:
    """
    使用された文字列を辞書で保持しておく
    すでにキーが存在していたら、重複文字とみなす
    O(n)
    """
    d = {}
    # O(n)
    for char in s:
        if char not in d:  # key in dict はO(1)
            d[char] = True
        else:
            return False
    return True


def inplace_sort(s: str) -> str:
    # python の文字列はimmutableなので、位置的にlistにキャストする
    s = list(s)
    # ちょっと実装めんどくさい・・・
    # インプレースマージソートなどでO(n log n)でできる
    s.sort()
    s = "".join(s)

    return s


def check2(s: str) -> bool:
    """
    sをインプレースにソートして、前から重複文字がないかチェックしていく
    O(n log n)
    """
    # インプレースにソートする。
    # O(n log n)
    inplace_sort(s)

    # 前から順番に、次の文字とかぶってないかチェックしていく
    # O(n)
    for index, char in enumerate(s):
        if (index != len(s) - 1) and (s[index] == s[index + 1]):
            return False

    return True
