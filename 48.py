#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 48.py

@time: 2019/5/24 22:38

@desc:

'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 旋转90度，一直是四个角落元素的顺指针替换，外圈完成之后，矩阵左右上下都缩减1格，继续重复
        n = len(matrix)
        row = 0  # 记录当前旋转的是第几行
        while row < n // 2:  # 若最后的矩阵只有一个元素，或没有元素，则结束
            for i in range(n-1-2*row):  # 这里的i是一个从0开始的递增量
                matrix[row][row+i], matrix[row + i][n - 1 - row], matrix[n - 1 - row][n - 1 - row - i], matrix[n - 1 - row - i][row] \
                    = matrix[n - 1 - row - i][row], matrix[row][row + i], matrix[row + i][n - 1 - row], matrix[n - 1 - row][
                    n - 1 - row - i]
            row += 1


if __name__ == '__main__':
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    res = Solution()
    res.rotate(matrix)
    print(matrix)
