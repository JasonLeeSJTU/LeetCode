#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 46.py

@time: 2019/5/16 22:51

@desc:

'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        # swap nums[0] with all the other positions
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]

            temp = self.permute(nums[1:])
            for val in temp:
                val = [nums[0]] + val
                res.append(val)

            # 换回来，保证下次交换0和其他位置的元素值，可以得到正确的结果
            nums[0], nums[i] = nums[i], nums[0]

        return res
