#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 134.py

@time: 2019/6/8 23:11

@desc:

'''
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        start = 0
        for i in range(len(gas)):
            start = i
            res = res + gas[i] - cost[i]
            j = i+1
            while j < len(gas):
                if res < 0:
                    res = 0
                    break
                else:
                    res = res + gas[j] - cost[j]
                    j += 1
            if j == len(gas):
                if res < 0:
                    res = 0
                    break
                j = 0
                while j < start:
                    res = res + gas[j] - cost[j]
                    if res < 0:
                        res = 0
                        break
                    j += 1

                if j == start:
                    return start
        return -1

    def best(self, gas, cost):
        # 存储的汽油总量，如果小于需要花费的汽油总量，则不可能实现循环。
        if sum(gas) < sum(cost):
            return -1
        # 否则一定存在一个方式，实现循环访问
        start, res = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            res += g - c
            # 从a出发无法到达b（b是第一个无法到达的汽油站），则从a和b之间的任意一个汽油站出发，都不能到达b
            if res < 0:
                res = 0
                start = i + 1
        return start

if __name__ == '__main__':
    res = Solution()
    gas = [2,3,4]
    cost = [3,4,3]
    a = res.canCompleteCircuit(gas, cost)
    print(a)