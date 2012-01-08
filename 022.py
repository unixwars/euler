#!/usr/bin/env python

# Using names.txt a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out
# the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938 53 = 49714. What is the
# total of all the name scores in the file?

def value(name, i):
    v = lambda x: ord(x)-ord('A')+1
    return sum(map(v,name)) * i

data  = open('names.txt').read()
names = sorted(data.replace('"','').split(','))

assert value('COLIN',938) == 49714
print sum([value(names[i], i+1) for i in range(len(names))])

