#!/usr/bin/python3
"""
    Function that divide every element of the matrix
    by the div number
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of list
        div: integer or float different from zero
    Raises:
        TypeError:
                 * matrix must be a matrix (list of lists) of integers/floats
                 * Each row of the matrix must have the same size
                 * div must be a number
        ZeroDivisionError:
                 * division by zero
    Returns:
        Matrix divided by div element
    """
    n = []
    cont, tam = 0, 0
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"

    if (not matrix) or type(matrix) is not list:
        raise TypeError(message1)

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for small in matrix:

        if type(small) is not list or not small:
            raise TypeError(message1)

        if cont == 0:
            tam = len(small)

        else:
            if tam != len(small):
                raise TypeError(message2)

        for elem in small:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(message1)

        cont = cont + 1

    n = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (n)
