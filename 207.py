#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 207.py

@time: 2019/6/10 15:18

@desc:

'''
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # 统计每门课程的先修课
        degree = [0 for i in range(numCourses)]
        post = collections.defaultdict(list)
        for i, j in prerequisites:
            degree[i] += 1 # 统计每门课程具有的先修课的数量
            post[j].append(i) # j是所有i的先修课

        # 所有没有先修课的课程，都先修读
        seq = [x for x in range(numCourses) if degree[x] == 0]
        res = []
        while seq:
            course = seq.pop()
            res.append(course)
            for i in post[course]:
                degree[i] -= 1
                if degree[i] == 0:
                    seq.append(i)

        if len(res) != numCourses:
            return False
        else:
            return True