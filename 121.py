#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 121.py

@time: 2019/6/22 15:16

@desc:

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy, sell = float('-inf'), float('-inf')
        for i in prices:
            buy = max(buy, -i)
            sell = max(sell, buy + i)
        return sell