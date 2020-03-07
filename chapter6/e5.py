import unittest


class Little:
    """
    水の単位リットルを表現するクラス
    """

    # 水を使える最小単位
    MIN_UNIT = 1

    def __init__(self, value):
        # 初期値はintしか受け付けない
        # => 取り扱える最小単位は1リットル（1リットル単位でしか水は扱えない）ことを暗に規定している
        if not isinstance(value, int):
            raise TypeError("'Little Object' can be initialized only with 'int'")
        self.__value: int = value

    def __add__(self, other):
        # リットルはリットルとしか演算できない
        if not isinstance(other, Little):
            raise TypeError("'Little Object' can be added only with 'Little Object'")
        # 演算時には新しいインスタンスを返す（イミュータブル）
        return Little(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, Little):
            raise TypeError("'Little Object' can be subbed only with 'Little Object'")

        return Little(self.value - other.value)

    def __eq__(self, other):
        # 比較演算子を定義しておくと、max等の関数に食わせることができる
        if not isinstance(other, Little):
            raise TypeError("'Little Object' can be compared only with 'Little Object'")

        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Little):
            raise TypeError("'Little Object' can be compared only with 'Little Object'")

        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, Little):
            raise TypeError("'Little Object' can be compared only with 'Little Object'")

        return self.value > other.value

    @property
    def value(self):
        return self.__value


MIN_LITTLE = Little(1)


class Jag:
    """
    壺を表現するオブジェクト
    ・壺ごとに最大容量が決まっており、最大容量以上の水はいれられない（容量以上の水はあふれて失われるとする）
    ・内容調は0未満には減らせない。（空っぽなので。やろうとしたら例外を創出する）
    ・壺に何リットル入っているか、あと何リットル入れられるかは分からない
    ・壺がいっぱいになっていることは分かる。
    ・壺が空になっていることは分かる
    """

    def __init__(self, max_volume: int = 0):
        # 最大容量
        self.max_volume: Little = Little(max_volume)
        # 現在の内容量（外部からはアクセスできない）
        self._volume: Little = Little(0)

    def increase(self, volume: Little):
        # 水を増やす
        # 最大容量を超えた分は失われる
        self._volume = min(self.max_volume, self._volume + volume)

    def decrease(self, volume: Little):
        # 水を減らす
        if self._volume < volume:
            # 現在容量を超えて減らすことはできない
            raise ValueError("You can not decrease volume over jag's current volume.")

        self._volume -= volume

    def is_full(self):
        # 壺がいっぱいかどうかを返す
        return self._volume == self.max_volume

    def is_empty(self):
        return self._volume == Little(0)


class Well(Jag):
    """
    ちゃんと表現するのがめんどくさいので、井戸は10万リットルの水が入った壺っていうことにする
    """

    def __init__(self):
        super().__init__()
        self.max_volume = Little(99999)
        self._volume = Little(99999)


class JagManager:
    """
    壺をアレコレする人
    ・壺から壺へ水を移すことができる
    　=> ただし、壺に何リットル入っているかは知ることができないので、
    　　　どちらかが空になるか、どちらかがいっぱいになるまで移すことしかできない
    ・壺に入っている水を捨てることができる
    　=> ただし、壺に何リットル入っているかは知ることができないので、空にすることしかできないとする

    """

    def pour(self, target: Jag, source: Jag) -> "JagManager":
        """
        targetの壺を、sourceの水でいっぱいにする
        """

        # targetがいっぱいになるか、sourceが空になるまで水を移す
        # あとどれぐらいの量入るか正確には分かららないので、少しずつ水を移す
        while not target.is_full() and not source.is_empty():
            source.decrease(MIN_LITTLE)
            target.increase(MIN_LITTLE)

        return self

    def empty(self, jag: Jag) -> "JagManager":
        """
        壺を空にする
        """
        # あとどれぐらいの量入るか正確には分かららないので、空になるまで少しずつ水を捨てる
        while not jag.is_empty():
            jag.decrease(MIN_LITTLE)

        return self


class Test(unittest.TestCase):
    def test_solve(self):
        well = Well()
        jag5 = Jag(5)
        jag3 = Jag(3)

        human = JagManager()
        human.pour(  # jag5を井戸水でいっぱいにする------------------------------------
            jag5, well
        ).pour(  # jag3をjag5の水でいっぱいにする
            jag3, jag5
        ).empty(  # jag3を空にする
            jag3
        ).pour(  # jag3にjag5の水を移す
            jag3, jag5
        ).pour(  # jag5を井戸水でいっぱいにする
            jag5, well
        ).pour(  # jag3をjag5の水でいっぱいにする
            jag3, jag5
        )

        assert jag5._volume == Little(4)  # jag5が4リットルになってるでしょ？


if __name__ == "__main__":
    unittest.main()
