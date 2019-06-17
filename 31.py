#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 31.py

@time: 2019/6/17 15:26

@desc:

'''
import bisect
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums) - 1
        # 从右向左查找，找到第一个升序排列的位置
        while i-1 >= 0 and  nums[i] <= nums[i-1]:
            i -= 1
        # 把i-1与刚好比num[i-1]略大的位置j，元素互换
        if i == 0: # 到了最左端，说明整个数组都是降序排列的
            nums[:] = nums[::-1]
            return

        # 从i开始往右找位置j, nums[i:]是降序排列的
        # j = bisect.bisect_left(nums, nums[i-1], i, len(nums)-1) # 只针对升序排序的数组有效
        # 二分查找
        if nums[-1] > nums[i-1]:
            j = len(nums) # 直接交换最后一个
        else:
            lo = i
            hi = len(nums) - 1
            while lo < hi:
                mid = (lo+hi) // 2
                if nums[mid] > nums[i-1]:
                    lo = mid + 1
                else:
                    hi = mid
            j = lo
        # j = i
        # while j < len(nums) and nums[j] > nums[i-1]:
        #     j += 1
        nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
        temp = nums[i:]
        nums[i:] = temp[::-1]

if __name__ == '__main__':
    nums = [1,3,2,1]
    res = Solution()
    res.nextPermutation(nums)
    print(nums)