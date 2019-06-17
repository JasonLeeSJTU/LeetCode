#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 560.py

@time: 2019/6/17 23:21

@desc:

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        self.count = 0

        def dfs(idx, residual):
            if residual == 0:
                self.count += 1
                return
            else:
                if idx + 1 < len(nums):
                    dfs(idx+1, residual - nums[idx+1])

        if not nums:
            return 0
        # 如果nums全是0，且k=0，则有n + n-1 + n-1 + ... + 1中组合
        if not any(nums):
            return len(nums) * (len(nums) + 1) // 2

        for i in range(len(nums)):
            dfs(i, k-nums[i])
        return self.count

    def better(self, nums, k):
        # 累加和cumsum
        # 则 i:j之间的子数组和为 cumsum[j] - cumsum[i]，可以直接判断是否等于k
        if not nums:
            return 0
        cumsum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums)+1):
            cumsum[i] = cumsum[i-1] + nums[i-1]

        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if cumsum[j] - cumsum[i] == k:
                    count += 1

        return count

    def best(self, nums, k):
        # 累加求和cumsum
        # 如果cumsum[j] - cumsum[i] = k，则在此之前，出现了几次cumsum[i]，就有几个满足条件的和为k的子序列
        # Let's remember count[V], the number of previous prefix sums with value V.
        # If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer.
        # This is because at time t, A[0] + A[1] + ... + A[t-1] = W,
        # and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V.
        # Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.
        dict = {0: 1}
        cumsum = 0
        count = 0
        for i in nums:
            cumsum += i
            count += dict.get(cumsum-k, 0)
            dict[cumsum] = dict.get(cumsum, 0) + 1
        return count