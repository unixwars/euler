# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Surprisingly there are only three numbers that can be written as the
# sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of
# fifth powers of their digits.

# Discussion: No 7 (or higher) digit number can be a possible solution
# since 7*9^5 is much less than 9999999. Hence, we try all 1 through 6
# digit numbers us

import euler

LIMIT = 6*(9**5) # 354294
POWER = 5
def check (num, power):
    digits = map(int, str(num))
    if num == sum(map(lambda x: x**power, digits)):
        return True

@euler.benchmark
def test():
    nums = []
    for x in xrange(2,LIMIT):
        if check(x, POWER):
            nums.append(x)

    print nums, sum(nums)

test()
