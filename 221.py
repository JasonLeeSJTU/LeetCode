#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 221.py

@time: 2019/6/17 20:14

@desc:

'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 动态规划，从右下角往左上角递推
        if not matrix:
            return 0
        # dp存储的是边长，最后结果需要平方一下
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp[i][-1] = matrix[i][-1] == '1'
        for j in range(len(matrix[0])):
            dp[-1][j] = matrix[-1][j] == '1'
        for i in range(len(matrix)-1)[::-1]:
            for j in range(len(matrix[0])-1)[::-1]:
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1]) + 1 # 三个位置，取最小的进行递增

        # return max([x**2 for row in dp for x in row])
        return max(map(max, dp))**2