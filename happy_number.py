#!/usr/bin/env python
# encoding: utf-8
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        hash = set()
        hash.add(n)
        sum = 0
        while True:
            while n !=0: # be careful here. I first make it to n%10 !=0
                sum += (n%10)**2
                n /= 10
            if sum in hash:
                return False
            elif sum == 1:
                return True
            else:
                hash.add(sum)
                n = sum
                sum = 0


