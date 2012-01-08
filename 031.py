# -*- coding: utf-8 -*-
#!/usr/bin/env python

# In England the currency is made up of pound, £, and pence, p, and
# there are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p,
# 50p, £1 (100p) and £2 (200p). It is possible to make £2 in the
# following way: 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

# How many different ways can £2 be made using any number of coins?

# Discussion: at most, 1 way with 200p coins, 2 with 100p, ..., 200
# with 1p coins. Create giant truth table and see.

import euler

COINS = [200, 100, 50, 20, 10, 5, 2, 1]

# Combinations with unique coin type
# 1, 2, 4, 10, 20, 40, 100, 200

@euler.benchmark
def test():
    pass

test()
