#!/usr/bin/env python

# n! means n  (n  1)  ...  3  2  1
# For example, 10! = 10 x 9 x ...  3 x 2 x 1 = 3628800, and the sum of
# the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find
# the sum of the digits in the number 100!

import math
print sum([int(x) for x in str(math.factorial(100))])
