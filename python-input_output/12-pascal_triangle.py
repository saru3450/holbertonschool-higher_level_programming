#!/usr/bin/python3
"""
lists of integers representing the Pascal
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) == n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri(i + 1))
        tmp.append(i)
        triangle.append(tmp)
    return triangle
