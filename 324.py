#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 324.py

@time: 2019/6/3 16:48

@desc:

'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        leng = (len(nums) + 1) // 2  # 选择leng个最小值
        small = temp[:leng]
        large = temp[leng:]
        # 为了避免small中有数和large中的数相等的情况，倒着插入
        id = 0
        id_small = leng - 1
        id_large = len(large) - 1
        while id_small >= 0: # id_small总是大于等于id_large
            nums[id] = small[id_small]
            if id_large:
                nums[id+1] = large[id_large]
            id_small -= 1
            id_large -= 1
            id += 2

    def better(self, nums):
        nums.sort()
        length = len(nums[::2]) # 奇数位置的个数
        small = nums[:length]
        large = nums[length:]
        nums[::2], nums[1::2] = small[::-1], large[::-1]