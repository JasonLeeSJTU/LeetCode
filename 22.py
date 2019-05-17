#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 22.py

@time: 2019/5/17 10:14

@desc:

'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 0:
            return 0
        # f = [0, 1, 2]   # number of parentheses, f(n) = 3f(n-1) - 1
        p = [[""], ["()"], ["(())", "()()"]]  # solution set
        for i in range(3, n + 1):
            temp = []
            for j in p[i - 1]:
                temp.append("(" + j + ")")
                temp.append("()"+j)
                temp.append(j+"()")
            temp.pop()  # the last one is "()()()", its repeated
            p.append(temp)

        return p[n]
