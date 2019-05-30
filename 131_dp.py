#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 131_dp.py

@time: 2019/5/30 20:15

@desc:

'''
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 动态规划
        # dp[i]存储s[0:i+1]的所有回文组合
        # 迭代公式：dp[i] = dp[j] + s[j:i], j=0,1,...,i-1.其中s[j:i]是回文才累加
        if not s:
            return []
        def is_palindrome(s):
            return s == s[::-1]
        dp = {0: [[]]}
        for i in range(1, len(s) + 1):
            dp[i] = []
            for j in range(i):
                if is_palindrome(s[j:i]):
                    dp[i].extend([x + [s[j:i]] for x in dp[j]])
        return dp[len(s)]

    def better(self, s):
        # 使用list比dict更快？
        def isPal(s):
            return s == s[::-1]

        n = len(s) + 1
        dp = [[[]]] + [[] for _ in range(n - 1)]
        for i in range(1, n):
            for j in range(0, i):
                if isPal(s[j:i]):
                    dp[i] += [each + [s[j:i]] for each in dp[j]]
        return dp[-1]

    def best(self, s: str):
        # 记录s[j:i]是否是回文，存储到一个数组中isPal
        # isPal[j][i] = True 当 s[j]==s[i] and (isPal[j+1][i-1] or i-j<=2)
        isPal = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j] == s[i-1] and (isPal[j+1][i-1] or i - j <= 2):
                    isPal[j][i] = 1

        # def pal(s):
        #     return s == s[::-1]

        dp = [[] for i in range(len(s) + 1)]
        dp[0] = [[]]
        for i in range(1, len(s) + 1):
            for j in range(i):
                # if pal(s[j:i]):
                if isPal[j][i]:
                    dp[i] += [x+[s[j:i]] for x in dp[j]]
        return dp[-1]

if __name__ == '__main__':
    res = Solution()
    a = res.best('aab')
    # b = 'abc'
    # print(b[0:0])
    print(a)