# -*- coding: utf-8 -*-
# 1463_1로 만들기
'''
10 -> 9 -> 3 -> 1
5 -> 4 -> 2 -> 1
5 -> 4 -> 3 -> 1

'''
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def fibo(x):
    candidates = []
    for v in x:
        if v % 3 == 0:
            candidates.append(v/3)
        if v % 2 == 0:
            candidates.append(v/2)
        candidates.append(v-1)
    return candidates

count = 0
res = [N]
while True:
    if N == 1:
        break
    step = res
    res = fibo(step)
    count += 1
    if min(res) == 1:
        break

print(count)