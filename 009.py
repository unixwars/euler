#!/usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a b c, for
# which, a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There exists exactly one
# Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# Brute force method
def test_pythagoras (a,b,c):
    return a**2+b**2==c**2

def test_sum (a,b,c):
    return a+b+c==1000

def triplets (N):
    for c in range(N):
        for b in range(N-c):
            for a in range(N-c-b):
                if test_sum(a,b,c) and test_pythagoras(b,c,a):
                        print '%s^2*%s^2=%s^2 ; %s*%s*%s=%s' %(a,b,c,a,b,c,a*b*c)

triplets(1000)

