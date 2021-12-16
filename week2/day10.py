#!/usr/bin/env Python3
from collections import defaultdict
file = open('day10.txt')
lines = list(map(lambda x: x.strip(), file.readlines()))

points = { '(': 1, '[': 2, '{': 3, '<': 4 }
pop_condition = { ')': '(', ']': '[', '}': '{', '>': '<' }

scores = []
for line in lines:
    stack, is_corrupted = [], False
    for c in line:
        if c in {'(', '{', '[', '<'}: stack.append(c)
        else:
            if stack[-1] == pop_condition[c]: stack.pop()
            else:
                is_corrupted = True
                break
    if not is_corrupted:
        ans = 0
        while stack:
            ans = ans * 5 + points[stack.pop()]
        scores.append(ans)
    
print(sorted(scores)[len(scores) // 2])
