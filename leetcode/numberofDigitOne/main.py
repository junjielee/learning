#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/number-of-digit-one/
"""


class Solution(object):
    # @param {integer} n
    # @param {integer}
    def countDigitOne(self, n):
        count = 0
        if n <= 0:
            return 0
        pows, nums_less_ten_pows = self.__calculate_pows_and_numbers_less(n)
        ten_pows_less = 10 ** (pows - 1)
        while n >= 10:
            number_high_level = n / ten_pows_less
            # 计算最高位1的个数
            if number_high_level > 1:
                count += ten_pows_less
            elif number_high_level == 1:
                count += (n % ten_pows_less + 1)
            # 计算最高位整位数(例如:100,200,3000,500等)之前的数字,
            # 除最高位以外的1的个数
            # 例如n = 230, 计算200之前，除最高位1的个数
            count += number_high_level * nums_less_ten_pows[ten_pows_less]

            n %= ten_pows_less
            ten_pows_less /= 10

        if n >= 1:
            count += 1
        return count

    def __calculate_pows_and_numbers_less(self, n):
        """
        计算刚好大于n的10的幂的数中的幂pows，
        和一个字典数据：key为10的幂，value为少于对应key值的1的个数
        args:
            n为要计算的整数n
        return:
            pows and nums_less_ten_pows
        """
        pows = 0
        nums_less_ten_pows = {
            0: 0,
            1: 0,
            10: 1
        }
        while n >= 10 ** pows:
            pows += 1
        for i in xrange(1, pows):
            nums_less_ten_pows[10 ** i] = nums_less_ten_pows[
                10 ** (i - 1)] * 10 + 10 ** (i - 1)
        print nums_less_ten_pows
        return (pows, nums_less_ten_pows)
