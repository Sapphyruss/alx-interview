#!/usr/bin/python3
""" island perimeter algo """


def island_perimeter(grid):
    """ calculate island perimeter """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                # check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # check up neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
