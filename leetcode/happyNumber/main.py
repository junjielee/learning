#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/happy-number/
"""


class Solution(object):
    # @param {integer} n
    # @return {boolean} n
    def isHappy(self, n):
        occured_nums = set()
        while n != 1:
            n = sum([pow(int(i), 2) for i in str(n)])
            if n in occured_nums:
                return False
            else:
                occured_nums.add(n)
        return True
