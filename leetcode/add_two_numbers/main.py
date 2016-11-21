#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
problem: https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _sum = 0
        new_list = tmp_node = ListNode(_sum)

        while l1 is not None or l2 is not None or _sum:
            if l1 is not None:
                _sum += l1.val
                l1 = l1.next

            if l2 is not None:
                _sum += l2.val
                l2 = l2.next

            tmp_node.next = ListNode(_sum % 10)

            tmp_node = tmp_node.next
            _sum /= 10

        return new_list.next


if __name__ == "__main__":

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    r = s.addTwoNumbers(l1, l2)

    print r.val
    print r.next.val
    print r.next.next.val
