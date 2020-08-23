# 10870_

import sys

N = int(sys.stdin.readline())
memo = [False] * (N + 1) 
def fibo(x):
    if x == 0: return 0
    elif x == 1: return 1
    
    if memo[x]:
        return memo[x]
    else:
        memo[x] = fibo(x-1) + fibo(x-2)
        return memo[x]

print(fibo(N))