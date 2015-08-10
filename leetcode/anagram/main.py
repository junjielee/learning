#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        # 居然相同或者
        # if s == t:
        #     return False
        s_dict = dict()
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        # 判断是否有相同的字母
        for j in t:
            if j in s_dict:
                s_dict[j] -= 1
            else:
                return False
        # 判断key是否全为0, 即相同字母的个数是否相同
        for key in s_dict:
            if s_dict.get(key) != 0:
                return False
        return True
