# -*- coding: utf-8 -*-
#!/usr/bin/env python

# A positive fraction whose numerator is less than its denominator is
# called a proper fraction. For any denominator, d, there will be d1
# proper fractions; for example, with d = 12: 1/12 , 2/12 , 3/12 ,
# 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

# We shall call a fraction that cannot be cancelled down a resilient
# fraction. Furthermore we shall define the resilience of a
# denominator, R(d), to be the ratio of its proper fractions that are
# resilient; for example, R(12) = 4/11 . In fact, d = 12 is the
# smallest denominator having a resilience R(d) < 4/10 .

# Find the smallest denominator d, having a resilience R(d) <
# 15499/94744 .

import fractions

def resilience(N):
    resilient = lambda x,y: fractions.gcd(x, y) == 1
    k = 0
    for x in range(1,N):
        k += int(resilient(x,N))
    return fractions.Fraction(k, N-1)

K = fractions.Fraction (15499, 94744)
for x in range(892371480, 892371485):
    if resilience(x) < K:
        print x, resilience(x)
        break

