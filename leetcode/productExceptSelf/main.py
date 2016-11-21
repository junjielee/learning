#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        multiply_numbers = 1
        zero_numbers = 0
        for num in nums:
            if num != 0:
                multiply_numbers *= num
            else:
                zero_numbers += 1
        if zero_numbers == 1:
            return [0 if num else multiply_numbers for num in nums]
        elif zero_numbers > 1:
            return [0 for num in nums]
        else:
            return [multiply_numbers / num for num in nums]


test = [1, 2, 3, 4]
solution = Solution()
products = solution.productExceptSelf(test)
print products
