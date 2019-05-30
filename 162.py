#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 162.py

@time: 2019/5/30 12:44

@desc:

'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        id = 0
        while id < len(nums) - 1:
            if nums[id] < nums[id + 1]:
                id += 1
            else:
                break
        return id

    def binary_search(self, nums):
        # 使用二分查找法
        def search(nums, left, right):
            if left == right:
                return left
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                search(nums, left, mid)
            else:
                search(nums, mid + 1, right)

        return search(nums, 0, len(nums) - 1)

    def iterative_binary_search(self, nums):
        # 使用循环实现二分查找
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left