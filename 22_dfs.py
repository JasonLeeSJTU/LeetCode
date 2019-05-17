#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 22_dfs.py

@time: 2019/5/17 11:16

@desc:

'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # DFS solution
        res = []
        self.dfs(res, '', n, n)
        return res

    def dfs(self, res, string, leftRemain, rightRemain):
        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return
        if leftRemain == 0 and rightRemain == 0:
            res.append(string)
            return
        self.dfs(res, string + "(", leftRemain - 1, rightRemain)
        self.dfs(res, string + ")", leftRemain, rightRemain - 1)

if __name__ == '__main__':
    res = Solution()
    a = res.generateParenthesis(3)