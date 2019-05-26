#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 289.py

@time: 2019/5/26 15:36

@desc:

'''
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy
        rows = len(board)
        cols = len(board[0])
        temp = copy.deepcopy(board)
        for i in range(rows):
            for j in range(cols):
                count = 0
                if i - 1 >= 0:  # top
                    count += temp[i - 1][j]
                if i + 1 < rows:  # bottom
                    count += temp[i + 1][j]
                if j - 1 >= 0:  # left
                    count += temp[i][j - 1]
                if j + 1 < cols:  # right
                    count += temp[i][j + 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    count += temp[i - 1][j - 1]
                if i - 1 >= 0 and j + 1 < cols:
                    count += temp[i - 1][j + 1]
                if i + 1 < rows and j - 1 >= 0:
                    count += temp[i + 1][j - 1]
                if i + 1 < rows and j + 1 < cols:
                    count += temp[i + 1][j + 1]

                if count < 2:
                    board[i][j] = 0
                if count > 3:
                    board[i][j] = 0
                if count == 3:
                    board[i][j] = 1

if __name__ == '__main__':
    res = Solution()
    a = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    res.gameOfLife(a)
    print(a)
