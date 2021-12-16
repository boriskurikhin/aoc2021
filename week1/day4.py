#!/usr/bin/env Python3
delim = '\n'

f = open('day4.txt')
# lines = list(map(str, f.read().split(delim)))

# # print(lines)
lines = f.readlines()

draws = list(map(int, lines[0].split(',')))
all_boards = []
all_bools = []
current = []
current_bools = []

for b in lines[1:]:
    if b == '\n' or not b:
        if current:
            all_boards.append(current)
            all_bools.append(current_bools)
        current = []
        current_bools = []
        continue
    current.append(list(map(int, list(filter(lambda x: x, b.split(' '))))))
    current_bools.append([False] * len(current[0]))

all_boards.append(current)
all_bools.append(current_bools)

# print(all_bools)
# print(all_boards)

wins = [False] * len(all_boards)

for num in draws:
    for i in range(len(all_boards)):
        if wins[i]: continue
        board = all_boards[i]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == num:
                    all_bools[i][r][c] = True
                    total_sum = 0
                    for rr in range(len(board)):
                        for cc in range(len(board[rr])):
                            if not all_bools[i][rr][cc]:
                                total_sum += board[rr][cc]
                    # check row 
                    good = True
                    for j in range(len(board)):
                        if not all_bools[i][j][c]:
                            good = False
                    if good:
                        wins[i] = True
                        if all(wins):
                            print('result', num * total_sum)
                            exit(0)
                    good = True
                    for j in range(len(board[0])):
                        if not all_bools[i][r][j]:
                            good = False
                    if good:
                        wins[i] = True
                        if all(wins):
                            print('result', num * total_sum)
