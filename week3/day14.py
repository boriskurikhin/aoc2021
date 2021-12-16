#!/usr/bin/env Python3
from copy import deepcopy
from collections import Counter
import math
''' end of imports '''

file = open('day14.txt')
pattern_shifts = dict()

seq = file.readline().strip()
file.readline() ## skip newline

while True:
    line = file.readline()
    if not line: break
    f, t = line.split(' -> ')
    pattern_shifts[f] = t.strip()

patterns = Counter()
for i in range(len(seq) - 1):
    patterns[seq[i:i+2]] += 1

for _ in range(40):
    new_patterns = Counter()
    for p, v in patterns.items():
        if len(p) != 2: continue
        first, last = p[0], p[1]

        left = first + pattern_shifts[p]
        right = pattern_shifts[p] + last

        new_patterns[left] += v
        new_patterns[right] += v
    patterns = new_patterns

freq = Counter()

for p, v in patterns.items():
    freq[p[0]] += v
    freq[p[1]] += v

counts = freq.values()
ans = (max(counts) - min(counts)) // 2 + 1
print(ans)