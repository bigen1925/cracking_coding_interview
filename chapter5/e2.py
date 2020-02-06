import unittest


def double_to_binary_string(num: float):
    """
    nは 0 < n <1 のfloat
    """
    string = "0."

    while True:
        if len(string) > 32:
            string = "ERROR."
            break

        num = num * 2
        if num > 1:
            string += 1
            num = num - 1
        elif num < 1:
            string += 0

        if num == 0:
            break

    return string


class TestMain:
    def test_it(self):
        assert double_to_binary_string(0.5) == "0.1"
        assert double_to_binary_string(0.25) == "0.01"
        assert double_to_binary_string(0.75) == "0.11"
        assert double_to_binary_string(0.125) == "0.001"
        assert double_to_binary_string(0.5 + 0.125 + 0.03125) == "0.10101"

        assert double_to_binary_string(0.1) == "ERROR."


if __name__ == "__main__":
    unittest.main()
