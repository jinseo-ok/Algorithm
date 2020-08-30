# -*- coding: utf-8 -*-
# 2579_계단 오르기
import sys

n = int(sys.stdin.readline())
stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

stack = [stairs[0]]
stack.append(stairs[1] + stack[0])
stack.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

for i in range(3, n):
    stack.append(max(stairs[i] + stairs[i - 1] + stack[i - 3], stairs[i] + stack[i - 2]))

print(stack[-1])