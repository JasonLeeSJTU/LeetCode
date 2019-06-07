#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 55.py

@time: 2019/6/7 15:47

@desc:

'''
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.flag = False
        self.dfs(nums)
        return self.flag


    def dfs(self, nums):
        if self.flag or not nums or len(nums) == 1:
            self.flag = True
            return True
        steps = nums[0]
        if steps >= len(nums[1:]):
            self.flag = True
            return True
        if steps == 0:
            return False
        for i in range(steps, 0, -1):
            self.dfs(nums[i:])

    def dp(self, nums):
        if not nums or len(nums) == 1:
            return True
        # 从右向左迭代
        map = [-1 for i in range(len(nums))]
        map[-1] = 1 # 1表示由此到达末尾, -1表示不能
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                map[i] = -1
            else:
                max_j = min(len(nums)-1, nums[i]+i)
                for j in range(1, max_j+1):
                    if map[j] == 1:
                        map[i] = 1

        return map[0] == 1

    def best(self, nums):
        if not nums or len(nums) == 1:
            return True
        # 从右向左，如果i + nums[i] >= end，这说明位置i可以到达终点
        # 将end用i替换，对于左面的索引，如果能到达i，也就是新的end，说明也可以到达终点
        end = len(nums) - 1
        for i in range(len(nums)-1)[::-1]:
            if i + nums[i] >= end:
                end = i
        return end == 0


if __name__ == '__main__':
    res = Solution()
    a = res.best([3,2,1,0,4])
    print(a)