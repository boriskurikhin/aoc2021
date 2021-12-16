#!/usr/bin/env Python3
delim = '\n'

f = open('day2.txt')
lines = list(map(str, f.read().split(delim)))

x = 0
y = 0
aim = 0

for l in lines:
    if 'forward' in l:
        x += int(l[8:])
        y += aim * int(l[8:])
    elif 'up' in l:
        aim -= int(l[3:])
    else:
        aim += int(l[5:])
print(x, y, aim)
print(x * y)