from time import time


if __name__ == "__main__":
    ns = [10000, 100000, 1000000, 10000000, 100000000]

    for n in ns:
        s = "x" * n
        ls = ["x" for i in range(n)]

        # 文字列のスライスの実行時間を出力
        start = time()
        s[(n // 2) :]
        end = time()
        print(f"string slice n={n}: {end-start} s")

        # リストのスライスの実行時間を出力
        start = time()
        ls[(n // 2) :]
        end = time()
        print(f"list slice n={n}: {end-start} s")
