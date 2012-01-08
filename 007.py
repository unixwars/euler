#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13. What is the 10001st prime number?

import euler

x=0
for prime in euler.prime():
    x += 1
    if x == 10001:
        print prime
        break
