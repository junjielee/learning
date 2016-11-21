#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
problem: https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return None

    def other_two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in d:
                return [min(i, d[other_num]), max(i, d[other_num])]
            d[num] = i


if __name__ == "__main__":
    s = Solution()
    print s.twoSum([3, 2, 4], 6)
    print s.other_two_sum([3, 2, 4], 6)
