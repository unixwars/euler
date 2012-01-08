#!/usr/bin/env python

# Starting in the top left corner of a 2*2 grid, there are 6 routes
# (without backtracking) to the bottom right corner. How many routes
# are there through a 20*20 grid?

"""
Discussion:

  a    b    c    d
A 1    1    1    1

B 1    2    3    4

C 1    3    6    10

D 1    4   10    16


  0  1  2
0 1  1  1
1 1  2  3
2 1  3  6

From aA to bA it is 1 route, from bA to cA 1 route, etc. There are 2
possible routes for a 1x1 segment grid, 6 for a 2x2, 16 for a 3x3, ...
The numbers follow the distribution of the Tartaglia Triangle.
"""

import euler

@euler.benchmark
def tartaglia (N):
    grid = [[1]*N for x in range(N)]
    for i in range(1,N):
        for j in range(1,N):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[N-1][N-1]

print tartaglia (21)
