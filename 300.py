#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 300.py

@time: 2019/6/10 20:38

@desc:

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        # dp[i]是到位置i时，最大的LIS长度，需要与j<i的所有dp[j]进行对比
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))] # LIS至少是1，也就是元素自身

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)