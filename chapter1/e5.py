import sys


def _is_one_deleted_string(s1: str, s2: str) -> bool:
    """
    s1がs2のone_deletedになっているか判定
    complexity: O(n)
    """
    # s2がs1より1文字だけ長いとき以外はFalse
    if len(s2) - len(s1) != 1:
        return False

    # 以下、s1の前方から1文字ずつs2と一致しているかチェックする
    # ただし、one_deletedを許すので1文字までスキップできる
    skip_count = 0  # スキップした回数

    for i in range(0, len(s1)):  # O(n)
        # s1とs2のi番目同士(1文字スキップ済みの場合は、その次の文字）を比較していく
        if s1[i] != s2[i + skip_count]:
            if (skip_count == 1) or ((skip_count == 0) and (s1[i] != s2[i + 1])):
                # すでに1文字スキップ済み(skip_count=1)の場合は、ここでFalse
                # または、未スキップ(skip_count=0)でも、次の文字とも一致しない場合はFalse
                return False
            else:
                # ここにはskip_count=0でかつ、次の文字とは一致している場合なので、
                # skip_count = 1として続行する
                skip_count = 1
    return True


def _is_one_inserted_string(s1: str, s2: str) -> bool:
    """
    s1がs2のone_insertedになっているか判定
    complexity: O(n)
    """
    #  s2がs1のone_deletedになっていることと同値
    return _is_one_deleted_string(s2, s1)


def _is_one_replaced_string(s1: str, s2: str) -> bool:
    """
    s1がs2のone_replacedになっていることを確認する
    complexity: O(n)
    """
    mismatch = 0

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if mismatch == 0:
                mismatch += 1
            else:
                return False
    return True


def is_one_way(s1: str, s2: str) -> bool:
    """
    2つの文字列が、1回の編集(insert, delete, replace)だけの違いかどうかを判定
    片方向だけ調べればOK
    complexity: O(n)
    """
    return (
        _is_one_deleted_string(s1, s2)
        or _is_one_inserted_string(s1, s2)
        or _is_one_replaced_string(s1, s2)
    )


if __name__ == "__main__":
    args = sys.argv
    print(is_one_way(args[1], args[2]))
