#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is
# 9009 = 91 99. Find the largest palindrome made from the product of
# two 3-digit numbers.

def lp():
    k   = None
    tup = None
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if x == y: continue
            num = str(x*y)
            if num == num[::-1]:
                if int(num) > k:
                    k = int(num)
                    tup = (x,y)
    return k, tup

print lp()
