#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 378.py

@time: 2019/5/24 10:09

@desc:

'''


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq

        if not matrix:
            return -1
        cols = len(matrix[0])
        rows = len(matrix)

        heap = []
        # 把第一行压入优先级队列
        for i in range(cols):
            heapq.heappush(heap, (matrix[0][i], 0, i))  # 元素值、行号、列号

        while k > 0:
            x, row, col = heapq.heappop(heap)
            k -= 1
            if row + 1 >= rows:
                continue
            # 把与x同一列的下一个元素压入队列
            heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))

        return x