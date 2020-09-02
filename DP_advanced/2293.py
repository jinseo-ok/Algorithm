# -*- coding: utf-8 -*-
# 2293_동전 1
import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [[0] * n]