#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

"""

""" Main idea is to pass the accumulated information to its left and right children
Three are some options:
1. modify the child's val add parent's information to the val
2. pass it as an argument of recursion call
3. add an extra field to the treeNode"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        val = 0
        if root.left:
            root.left.val+=root.val*10
            val+=self.sumNumbers(root.left)
        if root.right:
            root.right.val+=root.val*10
            val+= self.sumNumbers(root.right)
        return val



    """ Option2"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sums(root,prev):
            if not root:
                return 0
            if not root.left and not root.right:
                return prev*10+root.val
            val = 0
            if root.left:
                val +=sums(root.left,prev*10+root.val)
            if root.right:
                val +=sums(root.right,prev*10+root.val)
            return val
        return sums(root,0)
