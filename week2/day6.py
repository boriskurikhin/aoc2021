#!/usr/bin/env Python3

file = open('day6.txt')
fish = list(map(int, file.read().split(',')))

fishes = { f: fish.count(f) for f in set(fish) }
for i in range(256):
    new_fishes = { i: fishes.get(i + 1, 0) for i in range(9)}
    new_fishes[6] += fishes.get(0, 0)
    new_fishes[8] += fishes.get(0, 0)
    fishes = new_fishes
        
print(sum(fishes.values()))
file.close()