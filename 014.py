#!/usr/bin/env python

# The following iterative sequence is defined for the set of positive
# integers: n/2 (n is even), 3n + 1 (n is odd). Using the rule above
# and starting with 13, we generate the following sequence: 13 40 20
# 10 5 16 8 4 2 1. It can be seen that this sequence (starting at 13
# and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1.

# Which starting number, under one million, produces the longest
# chain? NOTE: Once the chain starts the terms are allowed to go above
# one million.

cache = {0:0, 1:0} # speed up things for every precalculated sequence

def collatz (n):
    if n in cache:
        return cache[n]

    if n%2==0:
        cache[n] = 1 + collatz(n/2)
    else:
        cache[n] = 2 + collatz((n*3+1)/2)
    return cache[n]

limit = 1000000
print max([(x, collatz(x)) for x in xrange(limit,0,-1)],key=lambda x:x[1])
