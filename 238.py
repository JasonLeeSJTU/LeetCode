#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 238.py

@time: 2019/5/16 23:33

@desc:

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return 0
        res = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            res[i] = res[i] * nums[i - 1]

        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp = temp * nums[i + 1]
            res[i] = res[i] * temp

        return res
