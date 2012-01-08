# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Find the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.

# Discussion: To speed up things, make the following considerations
#
# 1) If the square of x ends in 0, x ends in 0. Thus, the square ends
# in 00, and our top ends in 900
# 2) If the square of x ends in 900, x can only end in 030 or 070.
# 3) Knowing that, we'll start with 1010101030
#    (sqrt(1020304050607080900)) + 20
import math
import re

top = int(math.sqrt(1929394959697989900)) + 1
i   = 1010101030

while True:
    if re.match('1.2.3.4.5.6.7.8.9.0', str(i**2)):
        print i
        break
    i += [40,60][i%100==70]
