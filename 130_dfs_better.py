#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 130_dfs_better.py

@time: 2019/6/1 17:39

@desc:

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 从边界开始查找，对'O'的位置进行dfs搜索，都置为'S'
        # 最后遍历整个数组，为'S'的位置，变为'O'，其他所有位置，变为'X'
        if not board:
            return 
        def dfs(board, i, j):
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'S'
                dfs(board, i-1, j)
                dfs(board, i+1, j)
                dfs(board, i, j-1)
                dfs(board, i, j+1)

        for i in range(len(board)):
            dfs(board, i, 0)
            dfs(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            dfs(board, 0, j)
            dfs(board, len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'