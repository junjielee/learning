#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/summary-ranges/
"""


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        string = []
        begin = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                string.append(self.__get_range(nums[begin], nums[i]))
                begin = i + 1
        string.append(self.__get_range(nums[begin], nums[len(nums) - 1]))
        return string

    def __get_range(self, begin, end):
        if begin == end:
            return str(begin)
        else:
            return '%s->%s' % (begin, end)


test = [0, 1, 2, 4, 5, 7]
test_one = [-1]
solution = Solution()
string = solution.summaryRanges(test_one)
print string
