# -*- coding: utf-8 -*-
# 2293_동전 1
import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k+1)]

dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
        print(c, dp)

print(dp[k])
