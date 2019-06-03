#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 50.py

@time: 2019/6/3 15:45

@desc:

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0:
            return 0
        sign = True
        if n < 0:
            n = -n
            sign = False
        res = x
        while n > 0:
            i, base = 1, x
            while i <= n:
                n -= i
                res *= base
                i += i
                base *= base

        return res if sign else 1/res