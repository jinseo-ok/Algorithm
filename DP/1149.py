# -*- coding: utf-8 -*-
#1149_RGB거리
import sys

N = int(sys.stdin.readline())

cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(cost)):
    