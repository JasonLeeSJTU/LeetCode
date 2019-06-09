#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 56.py

@time: 2019/6/9 21:29

@desc:

'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        coll = sorted(intervals, key=lambda c: c[0])
        res = []
        start, end = coll[0]
        for i, j in coll[1:]:
            if i <= end:
                end = max(end, j)
            else: # 不存在交集
                res.append([start, end])
                start = i
                end = j
        # 加入最后一个
        res.append([start, end])
        return res
