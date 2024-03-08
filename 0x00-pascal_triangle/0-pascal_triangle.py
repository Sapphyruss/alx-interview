#!/usr/bin/python3
""" Pascal's triangle """


def pascal_triangle(n):
    """triangle function"""
    triangle = []
    if n <= 0:
        return (triangle)
    for i in range(1, n + 1):
        if i == 1:
            triangle.append([1])
        else:
            new_row = [1]
            # -1 to go to prev row, -1 to account for zero index
            prev_row = triangle[i-2]
            new_row.extend(prev_row[j] + prev_row[j+1]
                           for j in range(len(prev_row)-1))
            new_row.append(1)
            triangle.append(new_row)
    return (triangle)
