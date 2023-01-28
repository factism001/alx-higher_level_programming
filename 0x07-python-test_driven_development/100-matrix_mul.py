#!/usr/bin/python3
"""
this function returns the multiplication between two matrix
the multiplication of matrices is only posible when the number of columns of
the first one is equal to the number of rows of the secon one:
example:
 A = 2X8 dimensions of A
 B = 8X4 dimensions of B
Result = 2X4
"""


def matrix_mul(m_a, m_b):
    """
    Args:
        m_a: matrix
        m_b: matrix
    Raises:
        TypeError:
                 * m_a must be a list
                 * m_b must be a list
                 * m_a must be a list of lists
                 * m_b must be a list of lists
                 * m_a should contain only integers or floats
                 * m_b should contain only integers or floats
                 * each row of m_a must be of the same size
                 * each row of m_b must be of the same size
       ValueError:
                 * m_a can't be emplty
                 * m_a can't be emplty
                 * m_a and m_b can't be multiplied
    Returns:
        the new matrix that is the multiplication of two matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for m_aa in m_a:
        if type(m_aa) is not list:
            raise TypeError("m_a must be a list of lists")

    for m_bb in m_b:
        if type(m_bb) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_b) == 1 and len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for m_aa in m_a:
        for i in m_aa:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for m_bb in m_b:
        for j in m_bb:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    primera = len(m_a[0])
    for new in m_a:
        if (primera != len(new)):
            raise TypeError("each row of m_a must be of the same size")

    primera = len(m_b[0])
    for new in m_b:
        if (primera != len(new)):
            raise TypeError("each row of m_b must be of the same size")

    col_m_a = len(m_a[0])
    fil_m_b = len(m_b)
    if col_m_a != fil_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    res = 0
    n1 = []
    new = []
    for ct1 in range(len(m_a)):
        for ct2 in range(len(m_b[0])):
            for i in range(len(m_b)):
                res = res + (m_a[ct1][i] * m_b[i][ct2])
            n1.append(res)
            res = 0
        new.append(n1)
        n1 = []
    return(new)
