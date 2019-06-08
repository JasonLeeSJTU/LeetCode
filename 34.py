#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 34.py

@time: 2019/6/8 22:09

@desc:

'''
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分法定位
        # 定位之后，使用过两个指针，左移、右移，确定边界
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        pos = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                pos = mid
                break
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        if pos == -1:
            return [-1, -1]
        else:
            # 查找范围
            i, j = pos, pos
            while i-1 >= 0 and nums[i-1] == target:
                i -= 1
            while j+1 < len(nums) and nums[j+1] == target:
                j += 1
            return [i, j]

    def better(self, nums, target):
        # 二分法定位
        # 左边界：如果nums[mid]>=target， right=mid
        # 右边界：如果nums[mid]<=target， left=mid
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        pos = -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        if left == len(nums) - 1:
            return [left, left] # 只有一个位置有target
        pos = left
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return [pos, left-1] if nums[left] != target else [pos, left]

if __name__ == '__main__':
    res = Solution()
    ar = [6,6]
    a = res.better(ar, 6)
    print(a)