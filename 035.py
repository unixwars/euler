#!/usr/bin/env python

# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime. There are
# thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97. How many circular primes are there below one
# million?

import euler
for p in euler.prime():
    if p > 10**2:#6:
        break
    primes.add(p)

circular = set()
for p in primes:
    
