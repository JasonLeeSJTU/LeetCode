#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 29_work.py

@time: 2019/6/1 15:11

@desc:

'''

class Solution:
    def divide(self, dividend, divisor):
        pos = (dividend < 0) == (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        quotient, remainder = 0, 0
        while a >= b:
            temp = b
            i = 1
            while a >= temp:
                a -= temp
                temp += temp
                quotient += i
                i += i
        if not pos:
            quotient = -quotient
        return min(max(quotient, -0x80000000), 0x7fffffff)


if __name__ == '__main__':
    res = Solution()
    print(res.divide(5, 2))