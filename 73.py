#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 73.py

@time: 2019/6/10 20:09

@desc:

'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            matrix[i] = [0 for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j] = 0

    def better(self, matrix):
        # 使用每一行和每一列的第一个元素，存储标记
        zero_col = 1 # 第一列单独标记，防止与第一行混淆
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zero_col = 0
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 先判断第二列到最后一列（如果先判断行，会把列信息覆盖）
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0 for j in range(len(matrix[0]))]

        # 最后判断第一列
        if not zero_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
