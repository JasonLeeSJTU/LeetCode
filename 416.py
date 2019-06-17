#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 416.py

@time: 2019/6/17 22:40

@desc:

'''
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: # 和为奇数，不可能等分
            return False
        nums.sort(reverse=True) # 先从大的元素开始分解
        # 深度优先搜索，直到将s/2分解为0，就找到了结果
        def dfs(idx, residual): # idx是当前已经使用的元素的索引
            if residual < 0:
                return False
            elif residual == 0:
                return True
            else:
                for i in range(idx, len(nums)):
                    if dfs(i+1, residual - nums[idx]):
                        return True
                return False
        return dfs(0, s >> 1)

    def better(self, nums):
        s = sum(nums)
        if s & 1:  # 和为奇数，不可能等分
            return False
        nums.sort(reverse=True)  # 先从大的元素开始分解
        seen = {0: True} # 记录分解达到过的数值，避免重复访问

        # 深度优先搜索，直到将s/2分解为0，就找到了结果
        def dfs(idx, residual):  # idx是当前已经使用的元素的索引
            if residual not in seen:
                seen[residual] = False
                if residual > 0:
                    for i in range(idx+1, len(nums)):
                        if dfs(i, residual - nums[i]):
                            seen[residual] = True
                            break
            return seen[residual]

        return dfs(0, s >> 1)

if __name__ == '__main__':
    res = Solution()
    nums = [1,2,5]
    a = res.canPartition(nums)
    print(a)