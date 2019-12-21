def rotate_matrix(matrix: list) -> list:
    """
    O(n^2)
    """
    from math import floor

    n = len(matrix) - 1

    for layer in range(0, floor(n / 2) + 1):
        # nb_loop = (n^2)/4 - n/2  -> O(n^2)
        rotate_layer(matrix, layer)

    return matrix


def rotate_layer(matrix: list, layer: int) -> list:
    """
    O(n - layer)
    """

    n = len(matrix) - 1

    for i in range(layer, n - layer):
        temp = matrix[layer][i]
        matrix[layer][i] = matrix[n - i][layer]
        matrix[n - i][layer] = matrix[n - layer][n - i]
        matrix[n - layer][n - i] = matrix[i][n - layer]
        matrix[i][n - layer] = temp

    return matrix


if __name__ == "__main__":
    from sys import argv

    n = int(argv[1])
    matrix = [[i + j * n for i in range(n)] for j in range(n)]

    print("input matrix:")
    for row in matrix:
        print(row)

    rotated = rotate_matrix(matrix)

    print("rotated matrix:")
    for row in rotated:
        print(row)
