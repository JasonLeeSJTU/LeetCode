#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 322.py

@time: 2019/6/3 20:31

@desc:

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 贪婪法的结果不对
        # 动态规划，列是钱数，行是零钱币值
        #     | j=0 | j=1 | j=2 | ... | j=11 |
        #     --------------------------------
        # i=1 |
        # i=2 |
        # i=5 |
        # 更新公式是：dp[i][j] = min{dp[i-1][j], dp[i][j-coins[i]] + 1}
        # 进一步可以简化成只用一个行向量dp[j]

        dp = [amount+1 for col in range(amount+1)] # 初始化为一个大数，便于后面使用min
        dp[0] = 0
        coins.sort()
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]] + 1) # 如果amount不能被找零，则dp[amount+1]仍等于amount+1

        return -1 if dp[-1] > amount else dp[-1]


    def bfs(self, coins, amount):
        # 广度优先搜索，根节点是amount，每一层都分别减去币值
        if amount == 0:
            return 0

        stack = [amount]
        seen = [0 for i in range(amount+1)]
        level = 0
        while stack:
            level += 1
            temp = []
            for node in stack:
                for i in coins:
                    new_value = node - i
                    if new_value == 0:
                        return level
                    elif new_value > 0:
                        if not seen[new_value]:
                            seen[new_value] = 1
                            temp.append(new_value)

            stack = temp
        return -1