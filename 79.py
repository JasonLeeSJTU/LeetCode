#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 79.py

@time: 2019/6/7 10:51

@desc:

'''
from typing import List
import collections

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        self.res = False
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    self.dfs(board, word[1:], i, j, visited)
                    visited[i][j] = 0
                    if self.res:
                        return True
        return False

    def dfs(self, board, word, i, j, visited):
        if self.res:
            return
        if not word:
            self.res = True
            return

        dir_row = [1, -1, 0, 0]
        dir_col = [0, 0, 1, -1]
        for k in range(4):
            new_row = i + dir_row[k]
            new_col = j + dir_col[k]
            if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]) and board[new_row][new_col] == word[0] and not visited[new_row][new_col]:
                visited[new_row][new_col] = 1
                self.dfs(board, word[1:], new_row, new_col, visited)
                visited[new_row][new_col] = 0 # 上面一句结束了都没返回，说明不符合，回溯。


    def better_exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        self.res = False
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.better_dfs(board, word, i, j, visited)
                if self.res:
                    return True
        return False

    def better_dfs(self, board, word, i, j, visited):
        if self.res:
            return
        if not word:
            self.res = True
            return
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[0] or visited[i][j]:
            return

        visited[i][j] = 1
        self.better_dfs(board, word[1:], i+1, j, visited)
        self.better_dfs(board, word[1:], i-1, j, visited)
        self.better_dfs(board, word[1:], i, j+1, visited)
        self.better_dfs(board, word[1:], i, j-1, visited)
        visited[i][j] = 0

    def best(self, board, word):
        # pre-check
        # 检查word中的字符，是否都包含在board中
        board_dict = collections.Counter(x for row in board for x in row)
        word_dict = collections.Counter(word)
        for key, num in word_dict.items():
            if board_dict[key] < num:
                return False
        # 找到所有起始坐标
        candidates = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == word[0]]
        self.res = False
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for x, y in candidates:
            self.better_dfs(board, word, x, y, visited)
            if self.res:
                return True
        return False

if __name__ == '__main__':
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    res = Solution()
    a = res.best(board, word)
    print(a)