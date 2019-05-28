#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 75.py

@time: 2019/5/28 14:41

@desc:

'''
import random
from typing import List

class Solution:
    def better(self, nums):
        # it is a Dutch national flag problem
        bottom, mid, top = 0, 0, len(nums) - 1
        mid_val = 1 # middle value
        while mid <= top:
            if nums[mid] < mid_val: # group into bottom
                nums[bottom], nums[mid] = nums[mid], nums[bottom]
                bottom += 1
                mid += 1
            elif nums[mid] > mid_val: # group into top
                nums[mid], nums[top] = nums[top], nums[mid]
                top -= 1
            else:
                mid += 1 # group into mid, don't change


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # quick sort
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, start, end):
        if start == end:
            return
        id = self.partition(nums, start, end)
        if id > start:
            self.quick_sort(nums, start, id - 1)
        if id < end:
            self.quick_sort(nums, id +1, end)

    def partition(self, nums, left, right):
        idx = random.randint(left, right)
        nums[left], nums[idx] = nums[idx], nums[left]
        i, j = left, right
        while True:
            while i < right and nums[i] <= nums[left]:
                i += 1
            while j > left and nums[j] > nums[left]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        return j

if __name__ == '__main__':
    arr = [1, 2, 0]
    res = Solution()
    # res.sortColors(arr)
    res.better(arr)
    print(arr)