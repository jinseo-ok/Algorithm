# -*- coding: utf-8 -*-
# 9095_1,2,3 더하기
import sys
T = int(sys.stdin.readline())

def fibo(n):
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4
    else:
        return fibo(n-1) + fibo(n-2) + fibo(n-3)

for _ in range(T):
    N = int(sys.stdin.readline())
    res = fibo(N)
    print(res)
    

