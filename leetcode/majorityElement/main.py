#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    # @param {integer[]} nums
    # @return {integer}]
    def majorityElement(self, nums):
        """
        每次删除不同的两个数，那个majority element的数字
        还是数组中的majority element
        """
        times = 0
        for num in nums:
            if times == 0:
                majority = num
                times += 1
            else:
                if majority == num:
                    times += 1
                else:
                    times -= 1
        return majority
