#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 152.py

@time: 2019/6/3 19:58

@desc:

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 用fmax[i]记录以a[i]结尾的最大连续子串乘积
        # 用fmin[i]记录以a[i]结尾的最小连续子串乘积
        fmax = [0 for i in range(len(nums))]
        fmin = [0 for i in range(len(nums))]
        fmax[0] = nums[0]
        fmin[0] = nums[0]
        for i in range(1, len(nums)):
            fmin[i] = min(fmin[i-1]*nums[i], fmax[i-1]*nums[i], nums[i])
            fmax[i] = max(fmax[i-1]*nums[i], fmin[i-1]*nums[i], nums[i])

        return max(fmax)

    def best(self, nums):
        # 如果数组中没有0，则分为两种情况讨论：
        #     1. 如果包含偶数个负数，则全部元素相乘是最大乘积
        #     2. 如果包含奇数个负数，则又分为两种情况：
        #           i. 从开头到结尾一直乘，直到遇到最后一个负数终止
        #           ii. 从结尾往前一直乘，直到遇到第一个负数终止
        # 如果数组包含0，则0后面的连乘，就是数组值的本身
        temp = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1 # 从开头到结尾一直乘，遇到0，则乘积是自身
            temp[i] *= temp[i-1] or 1 # 从结尾到开头一直乘，遇到0，则乘积是自身
        return max(nums + temp) # nums + temp 是把两个数组合并