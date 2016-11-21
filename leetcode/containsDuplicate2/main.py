#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/contains-duplicate-ii/
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if nums is None:
            return False
        temp = {}
        for i in xrange(len(nums)):
            if temp.get(nums[i]) is None:
                temp[nums[i]] = i
            else:
                if i - temp[nums[i]] <= k:
                    return True
                else:
                    temp[nums[i]] = i
        return False

# nums = [0,1,2,3,0,4,5,6,7,8,9]
# k = 9
nums = [1]
k = 1
solution = Solution()
print solution.containsNearbyDuplicate(nums, k)
