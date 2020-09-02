# -*- coding: utf-8 -*-
# 9095_1,2,3 더하기
'''
1 = (1)
2 = (1+1), (2)
3 = (1+1+1), (1+2), (2+1), (3)
4 = (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1) 7개
5 = (1+1+1+1+1), (1+1+1+2), (1+2+1+1)... 17개
'''

import sys
T = int(sys.stdin.readline())

def fibo(x):
    if x == 1: return 1
    elif x == 2: return 2
    elif x == 3: return 4
    else:
        return fibo(x-1) + fibo(x-2) + fibo(x-3)

for _ in range(T):
    n = int(sys.stdin.readline())
    res = fibo(n)
    print(res)
