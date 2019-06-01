#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 91.py

@time: 2019/6/1 16:05

@desc:

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        # dfs
        self.count = 0
        def dfs(s):
            if not s:
                self.count += 1
                return
            if s[0] == '0':
                return
            for i in range(1, len(s) + 1):
                temp = int(s[:i])
                if temp >= 1 and temp <= 26:
                    dfs(s[i:])

        dfs(s)
        return self.count
    def dp(self, s):
        # 动态规划
        # f(n): 1. 把s[n]看做一个字符，如果不是0，则有f(n-1)中组合
        #       2. 把s[n]与s[n-1]组合起来，如果满足条件，则有f(n-2)种组合
        # f(n) = f(n-1) + f(n-2)
        if s[0] == '0':
            return 0
        f = [0 for i in range(len(s) + 1)]
        f[0] = 1
        f[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != '0':
                f[i] += f[i-1]
            if s[i-2] != '0':   # 一定要注意以0开始的字符串
                temp = int(s[i-2:i])
                if temp >= 1 and temp <= 26:
                    f[i] += f[i-2]

        return f[-1]

if __name__ == '__main__':
    res = Solution()
    print(res.dp("30"))
    print(res.dp("101"))
    print(res.dp("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
    # print(res.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
