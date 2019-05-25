#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 215.py

@time: 2019/5/25 22:36

@desc:

'''
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0 or k > len(nums):
            return -1
        self.flag = False
        self.res = 0
        self.helper(nums, 0, len(nums)-1, k)
        return self.res

    def helper(self, nums, start, end, k):
        if self.flag:
            return
        pos = self.partion(nums, start, end)
        if pos == len(nums) - k:
            self.flag = True
            self.res = nums[pos]
            return
        elif pos < len(nums) - k:
            self.helper(nums, pos + 1, end, k)
        else:
            self.helper(nums, start, pos - 1, k)

    def partion(self, nums, left, right):
        # 随机选择排序标准，防止最坏情况
        id = random.randint(left, right)
        nums[left], nums[id] = nums[id], nums[left]
        # 把小于nums[0]的数排到前面，大于nums[0]的数排到后面
        i = left
        j = right
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
    res = Solution()
    nums = [2, 1]
    a = res.findKthLargest(nums, 2)
    print(a)
