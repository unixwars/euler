#!/usr/bin/env python

# In the 5 by 5 matrix below, the minimal path sum from the top left
# to the bottom right, by only moving to the right and down, is
# indicated in bold red and is equal to 2427.
#
# *131	673	 234	 103	  18
# *201	*96	*342	 965	 150
# 630	803	*746	*422	 111
# 537	699	 497	*121	 956
# 805	732	 524	 *37	*331

# Find the minimal path sum, in matrix.txt, a 31K text file containing
# a 80 by 80 matrix, from the top left to the bottom right by only
# moving right and down.

# Discussion: the matrix.txt file provided can be solved by simply
# moving towards the smallest adjacent cell, but this approach is not
# valid for the sample 5x5 matrix since choosing a bigger cell may
# lead to a shorter path.

import euler

TEST = """131,	673,	234, 103,	18
201,	 96,	342, 965, 150
630,	803,	746, 422, 111
537,	699,	497, 121, 956
805,	732,	524,  37, 331"""

# Solution using graphs and Bellman-Ford
@euler.benchmark
def euler81a():
    # Create graph
    #
    lines = open('matrix.txt').readlines() #lines = TEST.split('\n')
    matrix = [map(int,[x for x in r.split(',')]) for r in lines]
    #
    # Entry point
    g = {(-1,0): {(0,0): matrix[0][0]}}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # exit point
            if i == len(matrix)-1 and j == len(matrix[i])-1:
                g[(i,j)] = {}

            # no nodes to the right
            elif j == len(matrix[i])-1:
                g[(i,j)] = {(i+1,j): matrix[i+1][j]}

            # no nodes beneath
            elif i == len(matrix)-1:
                g[(i,j)] = {(i,j+1): matrix[i][j+1]}

            # inner nodes
            else:
                g[(i,j)] = {(i+1,j):  matrix[i+1][j],
                            (i,j+1):  matrix[i][j+1]}

    # Solve
    #
    p, c = euler.bellman_ford(g, (-1,0))
    print c[(i,j)]


# Working naive solution, faster, but I'm not sure it is correct for
# all cases.
@euler.benchmark
def euler81b():
    lines = open('matrix.txt').readlines()
    A = [map(int,[x for x in r.split(',')]) for r in lines]
    N = 80
    B = []
    for i in range(N):
        B.append([0 for i in range(N)])

    B[0][0] = A[0][0]
    for i in range(1,N):
        B[i][0] = B[i-1][0]+A[i][0]
        B[0][i] = B[0][i-1]+A[0][i]

    for i in range(1,N):
        for j in range(1,N):
            B[i][j] = min(B[i-1][j],B[i][j-1])+A[i][j]

    print B[N-1][N-1]

euler81b()
euler81a()
