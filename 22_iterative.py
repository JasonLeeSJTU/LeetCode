#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 22_iterative.py

@time: 2019/5/17 11:30

@desc:

'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        left = 0
        right = 0
        res = []
        s = [('', left, right)]
        while s:
            string, left, right = s.pop()
            if left == n and right == n:
                res.append(string)
            if left < right or left > n or right > n:
                continue
            s.append((string + '(', left + 1, right))
            s.append((string + ')', left, right + 1))

        return res

if __name__ == '__main__':
    res = Solution()
    a = res.generateParenthesis(3)
    print(a)