#!/usr/bin/env python
# encoding: utf-8
"""
problem: https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        from Queue import Queue
        queue = Queue()
        if root is None:
            return root
        queue.put(root)
        while not queue.empty():
            cur_node = queue.get()
            temp_node = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = temp_node
            if cur_node.left:
                queue.put(cur_node.left)
            if cur_node.right:
                queue.put(cur_node.right)
        return root

    def invertTreewithRecursion(self, root):
        if root is None:
            return None
        temp = root.left
        root.left = self.invertTreewithRecursion(root.right)
        root.right = self.invertTreewithRecursion(temp)
        return root

# test
t4 = TreeNode(4)
t5 = TreeNode(5)

t2 = TreeNode(2)
t2.left = t4
t2.right = t5

t3 = TreeNode(3)
t1 = TreeNode(1)
t1.left = t2
t1.right = t3

solution = Solution()
solution.invertTreewithRecursion(t1)
if t1.right.right:
    print t1.right.right.val
