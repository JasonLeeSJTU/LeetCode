#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 54.py

@time: 2019/6/5 16:33

@desc:

'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix[0]
            matrix = self.rotate(matrix[1:])
        return res

    def rotate(self, matrix):
        # 把矩阵逆时针旋转90度
        if not matrix:
            return None
        temp = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp[j][i] = matrix[i][-j-1]
        return temp

    def better(self, matrix):
        if not matrix:
            return []

        def spiral_coordinate(r1, c1, r2, c2):
            for i in range(c1, c2+1):
                yield r1, i
            for i in range(r1+1, r2+1):
                yield i, c2
            if r1 == r2:
                return
            for i in range(c2-1, c1-1, -1):
                yield r2, i
            if c1 == c2:
                return
            for i in range(r2-1, r1, -1):
                yield i, c1

        res = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coordinate(r1, c1, r2, c2):
                res.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res

    def best(self, matrix):
        if not matrix:
            return []
        return [*matrix.pop(0)] + self.best([*zip(*matrix)][::-1])