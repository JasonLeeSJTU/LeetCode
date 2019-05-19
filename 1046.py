#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 1046.py

@time: 2019/5/19 10:33

@desc:

'''
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        while True:
            if len(stones) > 1:
                a = heapq.nlargest(2, stones)
                stones.pop(stones.index(a[0]))
                stones.pop(stones.index(a[1]))
                temp = a[0] - a[1]
                if temp:
                    stones.append(temp)
            else:
                break
        if stones:
            return stones[0]
        else:
            return 0

if __name__ == '__main__':
    res = Solution()
    a = res.lastStoneWeight([2,7,4,1,8,1])
    print(a)