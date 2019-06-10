#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 334.py

@time: 2019/6/10 19:14

@desc:

'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        # first < second < third
        first = second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second: # 第二个数比第一个数大
                second = i
            else:
                return True # 第三个数比前两个都大
        return False
