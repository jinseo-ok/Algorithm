# -*- coding: utf-8 -*-
# 121. Best Time to Buy and Sell Stock
import sys

class Solution:
    def maxProfit(self, prices):
        self.prices = prices
        p = 0
        for n in reversed(range(1, len(prices))):
            min_p = min(prices[:n])
            p = max(p, prices[n] - min_p)
        return p

prices = list(map(int, sys.stdin.readline().split()))
print(Solution().maxProfit(prices))