#!/usr/bin/env python

# A permutation is an ordered arrangement of objects. For example,
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all
# of the permutations are listed numerically or alphabetically, we
# call it lexicographic order. The lexicographic permutations of 0, 1
# and 2 are: 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1,
# 2, 3, 4, 5, 6, 7, 8 and 9?

# Discussion:
#
# math.factorial(9) = k = 362880 ==> permutations beginning with any
# given number. So k*2 < 10**6 < k*3, so the target is a permutiation
# beggining with the 3rd number of the string (#2). Similar reasoning
# can be followed with 8!, 7!, 6!, etc. Or... just generate all the
# permutations and select the nth one ;)

from itertools import permutations

i = 10**6
for x in permutations(range(10), 10):
    i -= 1
    if i == 0:
        print ''.join(map(str,x))
        break

# 2783915460
