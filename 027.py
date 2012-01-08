# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Euler published the remarkable quadratic formula: n² + n + 41. It
# turns out that the formula will produce 40 primes for the
# consecutive values n = 0 to 39.

# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
# by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible
# by 41. Using computers, the incredible formula n² - 79n + 1601 was
# discovered, which produces 80 primes for the consecutive values n =
# 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form: n² + an + b, where |a| < 1000
# and |b| < 1000. Find the product of the coefficients, a and b, for
# the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with n = 0.

import euler

MAX = 1000
k, x, y = None, None, None
f = lambda a,b,n: n**2+a*n+b
for a in xrange(-MAX+1, MAX):
    for b in xrange(-MAX+1,MAX):
        n = 0
        while True:
            if not euler.is_prime(f(a,b,n)):
                break
            n+=1
        if n>k:
            k, x, y = n, a, b
    print '%d/%d: [%d] (%d,%d)' %(MAX+a, MAX*2, k, x, y) # some feedback
    
print 'Solution: [%d]: n^2 + %dn + %d' % (k,x,y)
print 'Product:', x*y
