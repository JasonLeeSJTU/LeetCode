#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 15.py

@time: 2019/6/1 22:14

@desc:

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2): # 最少要有3个数，所以i索引最大len(nums) - 3
            if nums[i] > 0:
                break # 后面的数都大，和不可能为0了
            if i > 0 and nums[i] == nums[i-1]:
                continue # 避免重复，三数组形为(i, j, k)。i不能重复
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1 # 和太小，增大j
                elif sum > 0:
                    k -= 1 # 和太大，减小k
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # 对当前的i，找到了一组符合条件的之后，还要继续找其他的
                    j += 1
                    k -= 1
                    # 要避免重复
                    while j < k and nums[j] == nums[j-1]:
                        j += 1 # 因为j-1已经被记录了
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1 # 因为k+1已经被记录了
        return res