#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 17.py

@time: 2019/5/29 22:07

@desc:

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        string = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = list(string[digits[0]])
        for i in digits[1:]:
            temp = []
            for j in res:
                for k in string[i]:
                    temp.append(j + k)
            res = temp
        return res


    string = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    def recursion(self, comb, digits):
        if not digits:
            res.append(comb)
        for i in string[digits[0]]:
            self.recursion(comb+i, digits[1:])
    self.recursion([], digits)