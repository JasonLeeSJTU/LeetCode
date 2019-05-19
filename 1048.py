#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 1048.py

@time: 2019/5/19 11:00

@desc:

'''
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) <= 1:
            return len(words)
        dp = {}
        for w in sorted(words, key=len):
            for i in range(len(w)):
                dp[w] = max(dp.get(w, 1), 1 + dp.get(w[:i] + w[i+1:], 0))

        return max(dp.values() or [1])

if __name__ == '__main__':
    res = Solution()
    # a = res.check_predecessor('b', 'ba')
    a = res.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])
    print(a)