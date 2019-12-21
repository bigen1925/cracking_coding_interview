def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return is_substring(s1, s2 + s2)


def is_substring(s1: str, s2: str) -> bool:
    return s1 in s2


if __name__ == "__main__":
    from sys import argv

    print(is_rotation(argv[1], argv[2]))
