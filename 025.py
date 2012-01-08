#!/usr/bin/env python

# What is the first term in the Fibonacci sequence to contain 1000
# digits?

import euler

i = 0
for x in euler.fibonacci():
    i+=1
    if len(str(x)) == 1000:
        print i, x
        break
