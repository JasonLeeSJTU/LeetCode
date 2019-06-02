#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 179.py

@time: 2019/6/2 21:04

@desc:

'''
import random
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def compare(x, y):
            return -1 if x + y > y + x else (1 if x + y < y + x else 0)  # 逆序

        temp = sorted(map(str, nums), key=cmp_to_key(compare))
        temp = ''.join(temp)
        return '0' if temp[0] == '0' else temp

    def quick_sort(self, nums):
        def compare(x, y):
            return str(x) + str(y) > str(y) + str(x)

        def partition(nums, left, right):
            if left == right:
                return left
            base = random.randint(left, right)
            nums[left], nums[base] = nums[base], nums[left]
            l, r = left, right
            while l < r:
                while l < right and compare(nums[l], nums[left]): # 逆序
                    l += 1
                while r > left and not compare(nums[r], nums[left]):
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[left], nums[r] = nums[r], nums[left]
            return r

        def quickSort(nums, start, end):
            split = partition(nums, start, end)
            if split > start:
                quickSort(nums, start, split-1)
            if split < end:
                quickSort(nums, split+1, end)

        quickSort(nums, 0, len(nums)-1)
        temp = ''.join(map(str, nums))
        return '0' if temp[0] == '0' else temp