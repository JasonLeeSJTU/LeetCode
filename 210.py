#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 210.py

@time: 2019/6/9 13:01

@desc:

'''
from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 统计每个节点的邻近节点
        dict = collections.defaultdict(list)
        for i, j in prerequisites:
            dict[j].append(i)

        self.visited = [0 for i in range(numCourses)] #0表示未访问，1表示访问了，2表示到底了，没有邻近节点
        self.is_possible = True # 表示是否有环，有环则无法实现
        self.stack = [] # 存储序列
        # 深度优先搜索
        def dfs(node):
            if not self.is_possible:
                return

            self.visited[node] = 1

            if dict[node]:
                for i in dict[node]:
                    if self.visited[i] == 0: # 跳过标记为2的那些节点
                        dfs(i)
                    elif self.visited[i] == 1:
                        self.is_possible = False

            self.visited[node] = 2
            self.stack.append(node)

        for i in range(numCourses):
            if self.visited[i] == 0:
                dfs(i)

        return self.stack[::-1] if self.is_possible else []


if __name__ == '__main__':
    res = Solution()
    pre = [[0,1],[0,2],[1,2]]
    a = res.findOrder(3, pre)
    print(a)