def zeronize(matrix: list) -> None:
    """
    O(mn)
    """
    zero_rows = set()
    zero_columns = set()
    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        # O(mn)
        for column in range(n):
            if matrix[row][column] == 0:
                zero_rows.add(row)
                zero_columns.add(column)

    for row in range(m):
        # O(mn)
        if row in zero_rows:
            for column in range(n):
                matrix[row][column] = 0
        else:
            for column in zero_columns:
                matrix[row][column] = 0


if __name__ == "__main__":
    from sys import argv
    from random import random

    m = int(argv[1])
    n = int(argv[2])

    matrix = [[1 if random() < 0.9 else 0 for i in range(n)] for j in range(m)]

    print(f"input_matrix: ")
    for row in matrix:
        print(row)

    zeronize(matrix)

    print(f"zeronized_matrix:")
    for row in matrix:
        print(row)
