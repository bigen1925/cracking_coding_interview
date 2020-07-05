import unittest
from functools import reduce
from operator import or_
from typing import Set


def permutation(s: str) -> Set[str]:
    if len(s) == 1:
        return {s}

    perm = set()
    for char in s:
        sub_perm = permutation(s.replace(char, ""))
        perm |= {char + subs for subs in sub_perm}

    return perm


def pol(s: str) -> Set[str]:
    """permutation_one_line"""
    return reduce(or_, [{c + subs for subs in pol(s.replace(c, ""))} for c in s], set()) if len(s) - 1 else {s}

    # return reduce(
    #     or_,
    #     [{c + subs for subs in pol(s.replace(c, ""))} for c in s],
    #     set()
    # ) if len(s) - 1 else {s}


class Test(unittest.TestCase):
    def test(self):
        assert permutation("cba") == {"abc", "acb", "bac", "bca", "cab", "cba"}
        assert pol("cba") == {"abc", "acb", "bac", "bca", "cab", "cba"}


if __name__ == "__main__":
    unittest.main()
