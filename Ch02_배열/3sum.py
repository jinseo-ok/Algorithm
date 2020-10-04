# -*- coding: utf-8 -*-
# 15. 3Sum
import sys

class Solution:
    def threeSum(self, nums):
        self.nums = nums
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1] :
                continue
            left,right = i+1,len(nums)-1
            while left < right :
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0 :
                    temp = [nums[i],nums[left],nums[right]]
                    if res and res[-1] == temp:
                        pass
                    else:
                        res.append(temp)
                if summ > 0 :
                    right -= 1
                else:
                    left += 1
        return res

nums = list(map(int, sys.stdin.readline().split()))
print(Solution().threeSum(nums))