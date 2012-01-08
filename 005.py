#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder. What is the smallest
# positive number that is evenly divisible by all of the numbers from
# 1 to 20?

def divides_evenly (x, divisor_range):
    for y in divisor_range:
        if x % y != 0:
            return False
    return True

def check (start):
    x = start
    divisors = [11,12,13,14,15,16,17,18,19,20]

    while True:
        if divides_evenly(x, divisors):
            return x
        x+=1
        if x % 1000000 == 0:
            print 'Progress:',x

n = 2520
n = 232000000
#print divides_evenly (2520, [1,2,3,4,5,6,7,8,9,10])
ret = check(n) # 232792560
print 'Result:', ret

"""
This does not require programming at all. Compute the prime factorization of each number from 1 to 20, and multiply the greatest power of each prime together:

20 = 2^2 * 5
19 = 19
18 = 2 * 3^2
17 = 17
16 = 2^4
15 = 3 * 5
14 = 2 * 7
13 = 13
11 = 11

All others are included in the previous numbers.

ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560
"""

