#!/usr/bin/env python

# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to
# bottom in triangle.txt, a 15K text file containing a triangle with
# one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not
# possible to try every route to solve this problem, as there are 299
# altogether! If you could check one trillion (1012) routes every
# second it would take over twenty billion years to check them
# all. There is an efficient algorithm to solve it. ;o)

import euler

# Solution using graphs
@euler.benchmark
def euler67a():
    rows = [[-int(y) for y in x.split()] for x in open('triangle.txt').readlines()]
    g = {(-1,0): {(0,0): rows[0][0]}}

    for i in range(len(rows)-1):
        for j in range(len(rows[i])):
            g[(i,j)] = {(i+1,j):  rows[i+1][j],
                        (i+1,j+1):rows[i+1][j+1]}

    i = len(rows)-1
    for j in range(len(rows[i])):
        g[(i,j)] = {}

    p, c = euler.bellman_ford(g, (-1,0))
    print min([v for k,v in c.items() if k[0] == i])*-1

# Faster solution
@euler.benchmark
def euler67b():
    values = [[int(y) for y in x.split()] for x in open('triangle.txt').readlines()]
    values.reverse()
    for i in range(0, len(values) - 1):
        j = 0
        for k in values[i+1]:
            values[i+1][j] = max([int(k) + int(values[i][j]), int(k) + int(values[i][j+1])])
            j += 1
    print str(values[len(values)-1][0])

euler67b()

# Result: 7273
# Processing time: 20.026914 (euler67a)
# Processing time: 0.012345 (euler67b)

