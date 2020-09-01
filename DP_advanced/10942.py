# -*- coding: utf-8 -*-
# 10942_팬린드롬?
import sys


N = int(sys.stdin.readline())

p = list(map(str, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
qs = []
for _ in range(M):
    qs.append(list(map(int, sys.stdin.readline().split())))

temp = ''.join(p)

for q in qs:
    # print(q)
    l = int((q[1] - q[0]) / 2)
    if N == 1:
        print(1)
    elif (N == 2) and temp[q[0]-1] == temp[q[1]]:
        print(1)
    elif q[0] == q[1]:
        print(1)
    else:
        for j, i in enumerate(range(q[0]-1, q[1])):
            # print('temp:',temp[q[0]-1:q[1]])
            # print(temp[i], temp[q[1] - 1 - j])
            if j + 1 == int((q[1] - q[0] + 1) / 2):
                print(1)
                break
            # print((temp[q[0]-1 + l + j], temp[q[1] -1 - l - j]))
            if (temp[i] != temp[q[1] - 1 - j]) or (temp[q[0]-1 + l - j] != temp[q[1] -1 - l + j]):
                print(0)
                break
            