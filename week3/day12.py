#!/usr/bin/env Python3
from collections import defaultdict

''' end of imports '''
file, paths, edges = open('day12.txt'), set(), defaultdict(set)

lines = list(map(lambda x: x.strip(), file.readlines()))
for line in lines:
    start, finish = line.split('-')
    if finish != 'start': edges[start].add(finish)
    if start != 'start': edges[finish].add(start)

def go(node, path, twice, vis):
    if node == 'end': paths.add(path)
    else:
        for e in edges[node]:
            if e.islower():
                if e not in vis: go(e, f'{path}|{e}', twice, vis | {e})
                elif not twice: go(e, f'{path}|{e}', True, vis | {e}) 
            else: go(e, f'{path}|{e}', twice, vis)

go('start', 'start', False, {'start'})
print(len(paths))