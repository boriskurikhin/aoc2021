#!/usr/bin/env Python3
delim = '\n'

f = open('day3.txt')
lines = list(map(str, f.read().split(delim)))

N = 12

def find_last(lst, inverted=False):
    m_lst = list(map(lambda x: (x, x), lst))
    while len(m_lst) > 1:
        ones, zeros = 0, 0
        for line in m_lst:
            ones += int(line[0][0] == '1')
            zeros += int(line[0][0] == '0')
        if ones >= zeros: m_lst = list(filter(
            lambda x: x[0][0] == ('1' if not inverted else '0'), m_lst))
        else: m_lst = list(filter(
            lambda x: x[0][0] == ('0' if not inverted else '1'), m_lst))
        m_lst = list(map(lambda x: (x[0][1:], x[1]), m_lst))
    return int(m_lst.pop()[1], 2)

ans = find_last(lines) * find_last(lines, True)
print(ans)


# lines1 = list(map(lambda x: (x, x), lines))

# while True:
#     ones = 0
#     zeros = 0
#     # print(len(lines1))
#     if len(lines1) == 1:
#         print(lines1)
#         break
#     for line in lines1:
#         if line[0][0] == '1':
#             ones += 1
#         else:
#            zeros += 1
#     if ones >= zeros:
#         lines1 = list(filter(lambda x: x[0][0] == '1', lines1))
#     else:
#         lines1 = list(filter(lambda x: x[0][0] == '0', lines1))
#     lines1 = list(map(lambda x: (x[0][1:], x[1]), lines1))

# lines1 = list(map(lambda x: (x, x), lines))

# while True:
#     ones = 0
#     zeros = 0
#     # print(len(lines1))
#     if len(lines1) == 1:
#         print(lines1)
#         break
#     for line in lines1:
#         if line[0][0] == '1':
#             ones += 1
#         else:
#            zeros += 1
#     if ones < zeros:
#         lines1 = list(filter(lambda x: x[0][0] == '1', lines1))
#     else:
#         lines1 = list(filter(lambda x: x[0][0] == '0', lines1))
#     lines1 = list(map(lambda x: (x[0][1:], x[1]), lines1))
# one = defaultdict(int)
# zero = defaultdict(int)

# for i in range(N):
#     for line in lines:
#         if line[i] == '1':
#             one[i] += 1
#         else:
#             zero[i] += 1

# gamma = ''
# sigma = ''

# for i in range(N):
#     if one[i] > zero[i]:
#         gamma += '1'
#         sigma += '0'
#     else:
#         gamma += '0'
#         sigma += '1'

# print(gamma, sigma)#2849 