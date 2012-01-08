#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
# total. If all the numbers from 1 to 1000 (one thousand) inclusive
# were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three
# hundred and forty-two) contains 23 letters and 115 (one hundred and
# fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.

S = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
M = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def spell(N):
    s = ''

    if N>999:
        i, N = divmod(N, 1000)
        s += S[i] + ' thousand'

    if N>99:
        i, N = divmod(N, 100)
        s += S[i] + ' hundred'
        if N:
            s += ' and '

    if N>19:
        i, N = divmod(N, 10)
        s += M[i]
        if N:
            s += '-'
    if N:
        s+= S[N]
    return s

def count(s):
    return len(s.replace(' ','').replace('-',''))

k = 0
for x in range(1,1001):
    k += count(spell(x))

print k
