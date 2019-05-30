#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 8_regular_exp.py

@time: 2019/5/30 23:31

@desc:

'''
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        str = str.strip()
        str = re.search('^[+-]?\d+', str)
        if not str:
            return 0
        num = int(str.group())
        if num > 0x7fffffff:
            num = 0x7fffffff
        elif num < -0x80000000:
            num = -0x80000000
        return num

if __name__ == '__main__':
    str = ' -23ab'
    res = Solution()
    a = res.myAtoi(str)
    print(a)