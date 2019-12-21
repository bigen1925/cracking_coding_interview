def compress(s: str) -> str:
    """
    O(len(s))
    """
    compressed = ""
    prev = ""
    count = 0

    for char in s:
        if prev == char:
            count += 1
        else:
            if prev:
                compressed += prev + str(count)
            prev = char
            count = 1
    else:
        compressed += prev + str(count)

    result = compressed if len(compressed) < len(s) else s
    return result


if __name__ == "__main__":
    import sys

    print(compress(sys.argv[1]))
