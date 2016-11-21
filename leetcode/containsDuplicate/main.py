#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    # @param {integer[]} nums
    # @return {boolean)}
    def containDuplicate(self, nums):
        if nums is None:
            return False
        temp = dict()
        for i in xrange(len(nums)):
            if temp.get(nums[i]) is None:
                temp[nums[i]] = i
            else:
                return True
        return False

nums = [1, 1]
solution = Solution()
print solution.containDuplicate(nums)
