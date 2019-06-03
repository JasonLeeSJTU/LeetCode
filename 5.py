#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 5.py

@time: 2019/6/3 14:41

@desc:

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        self.res = s[0]
        self.max_len = 0
        self.dfs(s)
        return self.res

    def dfs(self, s):
        if not s:
            return
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                if i > self.max_len:
                    self.res = s[:i]
                    self.max_len = i
                self.dfs(s[i:])


    def is_palindrome(self, s):
        return s == s[::-1]

    def better(self, s):
        # 直接检查s[j:i]是否是回文
        if not s:
            return s
        isPal = [[0 if j!=i else 1 for i in range(len(s))] for j in range(len(s))]
        max_len = 0
        res = s[0]
        for i in range(1, len(s)):
            for j in range(i):
                if s[i] == s[j] and (isPal[j+1][i-1] or i-j<=2):
                    isPal[j][i] = 1
                    if i-j+1 > max_len:
                        max_len = i-j+1
                        res = s[j:i+1]
        return res
