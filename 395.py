#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 395.py

@time: 2019/6/10 19:06

@desc:

'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 找到s中出现次数小于k的第一个字符c，把s按照字符c分割，再对每个分割得到的字符串进行判断
        for c in s:
            if s.count(c) < k:
                return max([self.longestSubstring(i, k) for i in s.split(c)])
        # 一直没有返回值？说明整个字符串满足条件
        return len(s)