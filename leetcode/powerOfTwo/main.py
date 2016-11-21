#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/power-of-two/
"""


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0


test = range(21)
test.append(100)
solution = Solution()
for i in test:
    status = solution.isPowerOfTwo(i)
    print '%s -> %s' % (i, status)
