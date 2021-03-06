#!/usr/bin/env python
# encoding: utf-8

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!"""

""" Method1 Recursion by myself. So happy to get accepted the first submit!
The two sides are important! The lower one dicide the throughout height.
THe classic l<r condition in the while loop!
The time complexity is kind of high. it depens on the product of n and the values of product"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]: return 0
        def trapWithBar(bar):
            l = 0
            r = len(height)-1
            while l<r and height[l]<=bar:
                l+=1
            while l<r and height[r]<=bar:
                r-=1
            minHeight = min(height[l],height[r])
            if l>=r: return 0
            acc = 0
            for i in range(l+1,r):
                acc+=max(0,minHeight-max(bar,height[i]))
            return acc+trapWithBar(minHeight)

        return trapWithBar(0)



""" Method 2 change the recursive solution to iterative."""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]: return 0
        bar = 0
        acc = 0
        l = 0
        r = len(height)-1
        while True:
            while l<r and height[l]<=bar:
                l+=1
            while l<r and height[r]<=bar:
                r-=1
            minHeight = min(height[l],height[r])
            if l>=r: return acc
            for i in range(l+1,r):
                acc+=max(0,minHeight-max(bar,height[i]))
            bar = minHeight

        return acc
""" Method3 scan from left to right. Then scan from right to left. Take care of the equal condition.
Only one scan add the = part"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)==0:
            return 0
        tallest = height[0]
        total = 0
        potential = 0
        for i in range(1,len(height)):
            if tallest>=height[i]:
                potential+=tallest-height[i]
            else:
                total+=potential
                potential = 0
                tallest = height[i]
        # what we lack here is the water on the rightside of the tallest bar, add these back and scan from right to left
        potential = 0
        tallest1 = height[-1]
        for i in range(len(height)-2,-1,-1):
            if tallest1>height[i]:
                potential+=tallest1-height[i]
            else:
                total+=potential
                potential = 0
                tallest1 = height[i]
        return total

""" Modification on method3. When we approch the tallest bar, can break the second scan. But there's still unused computed
results which is in the first scan after the tallest bar"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)==0:
            return 0
        tallest = height[0]
        total = 0
        potential = 0
        for i in range(1,len(height)):
            if tallest>height[i]:
                potential+=tallest-height[i]
            else:
                total+=potential
                potential = 0
                tallest = height[i]
        potential = 0
        tallest1 = height[-1]
        for i in range(len(height)-2,-1,-1):
            if tallest1>=height[i]:
                potential+=tallest1-height[i]
            else:
                total+=potential
                potential = 0
                tallest1 = height[i]
                if tallest == tallest1:
                    break
        return total

""" Method 4. Smart one"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)==0:
            return 0
        left = 0
        right = len(height)-1
        leftMax = height[0]
        rightMax = height[-1]
        water = 0
        while left<right:
            if leftMax<rightMax:
                water += max(0,leftMax-height[left])
                left+=1
            else:
                water += max(0,rightMax-height[right])
                right -=1
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
        return water
""" A little Modification,but not obvious improvement"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)==0:
            return 0
        left = 0
        right = len(height)-1
        leftMax = rightMax = water = 0
        while left<right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
            if leftMax<rightMax:
                water +=leftMax-height[left]
                left+=1
            else:
                water += rightMax-height[right]
                right -=1

        return water





