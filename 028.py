# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is
# 101. What is the sum of the numbers on the diagonals in a 1001 by
# 1001 spiral formed in the same way?

# Discussion: The series is 1+2+2+2+2+4+4+4+4+6+6+6+6... Number of
# elements in both diagonals is SIDE*2 - 1.

def get_next():
    n = 1
    yield n # first elem
    k, i = 0, 0
    while True:
        if i%4 == 0:
            i  = 0
            k += 2
        n += k
        i += 1
        yield n

lst = []
for x in get_next():
    lst.append(x)
    if len(lst) == 2001:
        print sum(lst)    
        break

    
