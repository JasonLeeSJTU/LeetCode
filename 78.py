#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 78.py

@time: 2019/5/17 15:50

@desc:

'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        for i in range(len(nums) + 1):  # 0, 1, 2, 3, ..., n length of the subsets
            res += self.helper(nums, i)
        return res

    def helper(self, nums, n):  # get all subsets with length n
        if not nums:
            return
        if n == 0:
            return [[]]

        if n == 1:
            res = []
            for i in nums:
                res.append([i])
            return res

        res = []
        if len(nums) == n:
            res.append(nums)
            return res

        temp = self.helper(nums[1:], n-1)  # 包含nums[0]的n位subset
        for i in temp:
            res.append([nums[0]] + i)

        res += self.helper(nums[1:], n) # 不包含nums[0]的n位subset

        return res

if __name__ == '__main__':
    res = Solution()
    a = res.subsets([1,2,3,4])
    print(a)