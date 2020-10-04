# -*- coding: utf-8  -*-
# 238. Product of Array Except Self
import sys
from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        self.nums = nums
        s = [0 for i in range(len(nums))]
        if nums.count(0) == 1:
            z = list(filter(lambda x : x != 0, nums))
            for i in range(len(nums)):
                if nums[i] == 0:
                    s[i] = reduce(lambda x, y: x * y, z)
            return s
        elif nums.count(0) > 1:
            return s
        else:
            s = reduce(lambda x, y: x * y, nums)
            return [int(s / n) for n in nums]
        
nums = list(map(int, sys.stdin.readline().split()))
print(Solution().productExceptSelf(nums))