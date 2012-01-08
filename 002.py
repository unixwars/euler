#!/usr/bin/env python

# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

import euler

MAX = 4000000
num = 0
for x in euler.fibonacci():
    if x > MAX:
        break
    elif x % 2 == 0:
        num += x
print num
