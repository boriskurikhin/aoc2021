#!/usr/bin/env Python3:
from itertools import permutations

file = open('day8.txt')
lines = list(map(lambda x: x.strip(), file.readlines()))

ans = 0
valid = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}

for line in lines:
    first, second = line.split(' | ')
    first, second = first.split(' '), second.split(' ')
    mapping_function = None

    for comb in permutations('abcdefg'):
        maps_to = { a:b for a,b in zip(comb, 'abcdefg')}
        possible_remap = lambda word: ''.join(sorted([maps_to[let] for let in word]))
        if all((mapping in valid) for mapping in [possible_remap(w) for w in first]):
            mapping_function = possible_remap
            break

    assert mapping_function is not None, 'Mapping was not found. Something is broken'
    digits = int(''.join([str(valid[mapping_function(config)]) for config in second]))
    ans += digits


print(ans)
    