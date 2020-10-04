# -*- coding: utf-8 -*-
import sys

class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        dic1 = {n : i for i, n in enumerate(nums)}
        for i, v in enumerate(map(lambda x : target - x, nums)):
            if v in dic1.keys():
                if i != dic1[v]:
                    return [i, dic1[v]]


nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
print(Solution().twoSum(nums, target))