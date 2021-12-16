#!/usr/bin/env Python3

file = open('day7.txt')
lines = list(map(int, file.read().split(',')))
avg = sum(lines) / len(lines)
low_avg, hi_avg = int(avg - 0.5), int(avg + 0.5)
lower = sum([abs(k - low_avg) * (abs(k - low_avg) + 1) // 2 for k in lines])
upper = sum([abs(k - hi_avg) * (abs(k - hi_avg) + 1) // 2 for k in lines])
print(min(lower, upper))

