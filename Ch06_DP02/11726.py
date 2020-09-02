# -*- coding: utf-8 -*-
# 11726_2xn 타일링
import sys

n = int(sys.stdin.readline())

memo = {}

for i in range(1, n+1):
    if i == 1:
        memo[i] = 1
    elif i == 2:
        memo[i] = 2
    else:
        memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n] % 10007)