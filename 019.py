#!/usr/bin/env python

# You are given the following information, but you may prefer to do
# some research for yourself.

# 1 Jan 1900 was a Monday. Thirty days has September, April, June and
# November. All the rest have thirty-one, Saving February alone, Which
# has twenty-eight, rain or shine. And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a
# century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

# Discussion: 2000 leap year, so precisely 1/4 of years are. No need
# to contemplate exceptions to the rule.  1 Jan 1901 was Tuesday.

dpm  = [31,28,31,30,31,30,31,31,30,31,30,31]
dpml = [31,29,31,30,31,30,31,31,30,31,30,31]

day   = 2 # Tuesday
combo = 0

for year in range(1901,2001):
    months = [dpml,dpm][bool(year%4)]
    for x in months:
        day += x
        if day % 7 == 0:
            combo+=1
            
print combo
