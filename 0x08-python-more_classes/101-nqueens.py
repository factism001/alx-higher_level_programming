#!/usr/bin/python3
"""
Resolve NQUEEN Problem
"""


def check(queen, column):
    """
    function that checks if the position of each queen is valid
    """
    for i in range(column):
        if queen[i] == queen[column]:
            return False
        if abs(queen[i] - queen[column]) == abs(i - column):
            return False
    return True


def fulling(queen, column):
    """
    Recursive Function that change the queen when we
    get the correct position with no problems
    """

    tam = len(queen)
    exito = 0

    if column == tam:
        result = []

        for i in range(len(queen)):
            result.append([i, queen[i]])

        print(result)
        return True

    queen[column] = -1

    while(queen[column] < tam - 1 or exito == 1):
        queen[column] = queen[column] + 1
        if check(queen, column) is True:
            if column != tam:
                fulling(queen, (column + 1))
            else:
                exito = 1
                break
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = []
    tam = int(sys.argv[1])
    for i in range(tam):
        queen.append(-1)

    fulling(queen, 0)
