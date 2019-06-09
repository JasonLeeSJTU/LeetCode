#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 139.py

@time: 2019/6/9 15:09

@desc:

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        # 深度优先搜索
        def dfs(s, wordDict):
            if self.res:
                return
            if not s: # 分割完毕
                self.res = True
                return
            for i in wordDict:
                length = len(i)
                if s[:length] == i: #开头部分能够匹配
                    dfs(s[length:], wordDict)

        dfs(s, wordDict)
        return self.res

    def dp(self, s, wordDict):
        # 动态规划，对于索引位置i，如果s[:j]是true，并且s[j:i]存在于wordDict中，则s[:i]也是true
        f = [0 for i in range(len(s)+1)]
        f[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[-1] == True