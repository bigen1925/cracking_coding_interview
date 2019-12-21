import random, time


def urlify1(s: str, length: int) -> str:
    """
    たんに前から文字列を結合していく
    """
    s = s[0:length]  # O(n)
    ret = ""

    # O(n)
    for index, char in enumerate(s):
        # O(i)
        if char == " ":
            ret += "%20"
        else:
            ret += char

    return ret


def urlify2(s: str, length: int) -> str:
    """
    配列化して要素ごとに置き換えて、後からジョインする
    文字列結合回数が少なくて済むから早くなるかと思ったけど、そうでもなかった
    O(n)
    """
    s = s[0:length]  # O(n)
    ls = list(s)  # O(n)

    # O(n)
    for index, char in enumerate(ls):
        # O(1) <- わりと謎
        if char == " ":
            ls[index] = "%20"

    s = "".join(ls)  # O(n)
    return s


def speed_test():
    """
    urlify1と2でスピードに差があるか確認
    結果：2倍ぐらいスピード違うけど、オーダーはどっちもO(n)
    """
    ns = [1000, 10000, 100000, 1000000, 10000000]

    alphabet = ["a", " "]

    for n in ns:
        # 長さnの文字列を生成
        s = "".join([random.choice(alphabet) for x in range(0, n)])

        start = time.time()
        urlify1(s, n)
        print("urlifi1(n={}): {} s".format(n, start - time.time()))

        start = time.time()
        urlify2(s, n)
        print("urlifi2(n={}): {} s".format(n, start - time.time()))
        # urlifi1(n=1000): -0.00013685226440429688 s
        # urlifi2(n=1000): -6.985664367675781e-05 s
        # urlifi1(n=10000): -0.0012240409851074219 s
        # urlifi2(n=10000): -0.0006947517395019531 s
        # urlifi1(n=100000): -0.013718128204345703 s
        # urlifi2(n=100000): -0.006711006164550781 s
        # urlifi1(n=1000000): -0.13614487648010254 s
        # urlifi2(n=1000000): -0.0740208625793457 s
        # urlifi1(n=10000000): -1.4178009033203125 s
        # urlifi2(n=10000000): -0.7139589786529541 s


def test_concat():
    # pythonの文字列結合は、文字列の長さに依存するかテスト
    # 結果：O(1)　→　依存しない
    ns = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

    for n in ns:
        # 長さnの文字列
        s = "a" * n

        start = time.time()
        # 文字列を結合
        s += "a"
        print("str_concat(n={}) : {} s".format(n, time.time() - start))
        # str_concat(n=100) : 3.0994415283203125e-06 s
        # str_concat(n=1000) : 9.5367431640625e-07 s
        # str_concat(n=10000) : 4.0531158447265625e-06 s
        # str_concat(n=100000) : 2.86102294921875e-06 s
        # str_concat(n=1000000) : 4.0531158447265625e-06 s
        # str_concat(n=10000000) : 5.0067901611328125e-06 s
        # str_concat(n=100000000) : 8.106231689453125e-06 s


def test_concat_loop():
    # n回繰り返す文字列結合を行った場合、O(n)になるか確認
    # 結果：O(n)
    ns = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

    for n in ns:
        s = ""

        start = time.time()
        for i in range(n):
            s += "a"
        print("str_concat(n={}) : {} s".format(n, time.time() - start))
        # str_concat(n=100) : 2.288818359375e-05 s
        # str_concat(n=1000) : 0.00018095970153808594 s
        # str_concat(n=10000) : 0.0014069080352783203 s
        # str_concat(n=100000) : 0.015003204345703125 s
        # str_concat(n=1000000) : 0.10742330551147461 s
        # str_concat(n=10000000) : 1.0418879985809326 s
        # str_concat(n=100000000) : 10.299352169036865 s
