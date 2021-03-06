#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = walk = ListNode(0)

        while l1 and l2:
            if l1.val<l2.val:
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next
            walk = walk.next

        if l1:
            walk.next = l1
        elif l2:
            walk.next = l2
        return dummy.next
