# -*- coding: utf-8 -*-
# 2579_계단 오르기
import sys

n = int(sys.stdin.readline())
stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline().strip()))

if n < 4:
    print(sum(stairs))
else:   
    stack = []
    stack.append(stairs[0]) # stack[0]
    stack.append(stack[0] + stairs[1]) # stack[1]
    stack.append(max(stairs[0] + stairs[1], stairs[0] + stairs[2])) # stack[2]

    for i in range(3, n):
        stack.append(max(stairs[i] + stairs[i - 1] + stack[i - 3], stairs[i] + stack[i - 2]))
    print(stack[-1])