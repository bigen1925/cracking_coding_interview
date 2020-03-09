# 男女1カップルから生まれる女児の期待値は1、男児の数の期待値は
# 0人: 1/2
# 1人: 1/4
# 2人: 1/8
# ...
#
# E = sum_[k=0 -> inf] k * (1/2)^(k+1)
# 1/2 * E = 1/2 * sum_[k=0 -> inf] k * (1/2)^(k+1)
#         = sum_[k=0 -> inf] k * (1/2)^(k+2)
#         = sum_[K=1 -> inf] (K-1) * (1/2)^(K+1)
# E - (1/2 * E) = sum_[k=0 -> inf] k * (1/2)^(k+1) - sum_[K=1 -> inf] (K-1) * (1/2)^(K+1)
# <=> 1/2 * E = [k=0](k * (1/2)^(k+1)) + sum[k=1 -> inf] (1/2)^(k+1)
#             = 0 + 1/2
# <=> E = 1
#
# よって、1カップルから生まれる子供の数の期待値は、男児1人、女児1人となる
#
from enum import Enum
from random import choice


class GENDER(Enum):
    MAN = 1
    WOMAN = 2


class Child:
    def __init__(self, gender: GENDER):
        self.__gender = gender

    def is_man(self):
        return self.__gender == GENDER.MAN

    def is_woman(self):
        return self.__gender == GENDER.WOMAN


class Couple:
    def make_children(self):
        children = {"men": [], "women": []}
        while True:
            child = self.bear()
            if child.is_man():
                children["men"].append(child)
            elif child.is_woman():
                children["women"].append(child)
                break

        return children

    @staticmethod
    def bear():
        gender = choice([GENDER.MAN, GENDER.WOMAN])
        return Child(gender=gender)


if __name__ == "__main__":
    """
    10万回の試行で男女何人ずつ生まれるかテスト
    女児はぴったり10万人になるはず    
    """
    couple = Couple()
    make_count = 100000
    men_count = 0
    women_count = 0

    for i in range(make_count):
        children = couple.make_children()
        men_count += len(children["men"])
        women_count += len(children["women"])

    print(f"men: {men_count} / {make_count}")
    print(f"women: {women_count} / {make_count}")
