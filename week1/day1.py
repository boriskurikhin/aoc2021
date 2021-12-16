#!/usr/bin/env Python3
delim = '\n'

f = open('day1.txt')
lines = list(map(int, f.read().split(delim)))
start = lines[0] + lines[1] + lines[2]
count = 0

for i in range(1, len(lines) - 2):
    k = lines[i] + lines[i + 1] + lines[ i + 2]
    if k > start:
        count += 1
    start = k

print(count)