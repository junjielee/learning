#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    # @param {integer} n
    # @param {integer}
    def countDigitOne(self, n):
        count = 0
        if n <= 0:
            return 0
        for i in range(1, n + 1):
            temp = i
            while temp:
                if temp % 10 == 1:
                    count += 1
                temp = temp / 10
        return count
