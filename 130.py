#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 130.py

@time: 2019/6/1 17:07

@desc:

'''
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        keys = {}
        flag = 1

        def flip(board, i, j):
            if (i <= 0 or i >= len(board) - 1 or j <= 0 or j >= len(board[0]) - 1) and board[i][j] == 'O': # boarder
                keys.pop(flag, None)
                return

            if board[i][j] == 'O':
                board[i][j] = flag
                flip(board, i-1, j)
                flip(board, i+1, j)
                flip(board, i, j-1)
                flip(board, i, j+1)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                if board[i][j] == 'O':
                    keys[flag] = 1
                    flip(board, i, j)
                    flag += 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                elif board[i][j] in keys.keys():
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

if __name__ == '__main__':
    res = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    res.solve(board)
    print(board)