#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 33.py

@time: 2019/6/8 15:29

@desc:

'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if target <= nums[right]: #在后半部分
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        right = mid - 1
                    else:
                        return mid
            elif target >= nums[left]: #在前半部分
               if nums[mid] < nums[left]:
                   right = mid - 1
               else:
                   if target > nums[mid]:
                       left = mid + 1
                   elif target < nums[mid]:
                       right = mid - 1
                   else:
                       return mid
            else:
                return -1 #既不在前半部分，也不在后半部分
        return -1

    def better(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == '__main__':
    res = Solution()
    a = res.better([1], 0)
    print(a)
