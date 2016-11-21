#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node is None:
            return
        if node.next is not None:
            node_next = node.next
            node.val = node_next.val
            node.next = node_next.next
            del(node_next)
        else:
            node.val = None
            del(node)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
solution = Solution()


def print_node_tree(root):
    while root:
        print root.val
        root = root.next


def test(node):
    print_node_tree(node1)
    solution.deleteNode(node)
    print_node_tree(node1)

# test(node1)
# test(node2)
test(node4)
