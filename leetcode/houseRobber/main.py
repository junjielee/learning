#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/house-robber/
"""


class Solution(object):
    # @param {integer[]} nums
    # @return {integer}
    # 时间复杂度O(n)，空间复杂度O(n)
    def rob(self, nums):
        size = len(nums)
        max_before = [0] * (size + 1)
        if size:
            max_before[1] = nums[0]
        for i in (range(2, size + 1)):
            max_before[i] = max(max_before[i - 1], max_before[i - 2] + nums[i - 1])
            print max_before
        return max_before[size]

    # 时间复杂度O(n)，空间复杂度O(1)
    def rob_optimize(self, nums):
        size = len(nums)
        before, after = 0, 0
        for i in range(size):
            if i & 1:
                before = max(before + nums[i], after)
            else:
                after = max(after + nums[i], before)
        return max(before, after)
