#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 36.py

@time: 2019/5/27 15:54

@desc:

'''
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 先判断每一行
        for i in range(9):
            rows = {}
            for j in board[i]:
                if j != '.':
                    if j not in rows.keys():
                        rows[j] = 1
                    else:
                        return False

        # 判断每一列
        col_board = zip(*board)
        for i in range(9):
            cols = {}
            # temp = [item[i] for item in board] # 取出第i列元素
            # for j in temp:
            for j in col_board[i]:
                if j != '.':
                    if j not in cols.keys():
                        cols[j] = 1
                    else:
                        return False

        # 判断每一个3x3的方格
        for i in range(3):
            for j in range(3):
                box = {}
                for k in range(3):
                    for l in board[i * 3 + k][j * 3:j * 3 + 3]:
                        if l != '.':
                            if l not in box.keys():
                                box[l] = 1
                            else:
                                return False

        return True

    def better(self, board):
        all = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    all += [(i, c), (c, j), (i // 3, j // 3, c)] # i//3, j//3 makes 3x3 box into one block
        return len(all) == len(set(all)) #  all = [ (2, '2'), ('2', 2), ...]

if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "2", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    res = Solution()
    a = res.better(board)
    print(a)
