#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 309.py

@time: 2019/6/18 13:27

@desc:

'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # buy[i] 表示到第i天，以买入结尾，所得的最大收益
        # sell[i] 表示到第i天，以卖出结尾，所得的最大收益
        # buy[i] 分为两种情况：
        #   1. 第i天不买入，则 buy[i] = buy[i-1]
        #   2. 第i天买入，则卖出操作不能发生在第i-1天，因为要cooldown，则buy[i] = sell[i-2] - price
        # 综上：buy[i] = max(buy[i-1], sell[i-2] - price)
        # sell[i] 分为两种情况：
        #   1. 第i天不卖出，则 sell[i] = sell[i-1]
        #   2. 第i天卖出，则 sell[i] = buy[i-1] + price
        # 综上，sell[i] = max(sell[i-1], buy[i-1] + price)
        if len(prices) < 2:
            return 0
        buy = [0 for _ in range(len(prices))]
        sell = [0 for _ in range(len(prices))]
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], buy[0] + prices[1])
        for i in range(2, len(prices)):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
        return sell[-1]

    def better(self, prices):
        if len(prices) < 2:
            return 0
        buy = -prices[0]
        sell = 0
        prev_sell = 0
        for i in prices:
            prev_buy = buy
            buy = max(buy, prev_sell - i)
            prev_sell = sell
            sell = max(sell, prev_buy + i)
        return sell


if __name__ == '__main__':
    res = Solution()
    a = [1,2,3,0,2]
    print(res.maxProfit(a))
    print(res.better(a))
