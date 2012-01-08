#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum
# of all the primes below two million.

import euler

primes = []
for p in euler.prime():
    if p > 2000000:
        break
    primes.append(p)
    
print sum(primes)
