#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 166.py

@time: 2019/6/1 15:33

@desc:

'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        pos = (numerator < 0) == (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        quotient = str(numerator // denominator)
        if pos:
            res = quotient
        else:
            res = '-' + quotient
        remainder = numerator % denominator
        if not remainder:   #整除，没有小数点以及后面的数
            return res
        else:
            res += '.'

        map = {}
        remainder *= 10
        while remainder:
            if remainder not in map.keys():
                map[remainder] = len(res)
            else:
                i = map[remainder]
                res = res[:i] + '(' + res[i:] + ')'
                return res

            res += str(remainder // denominator)
            remainder = remainder % denominator
            remainder *= 10

        return res

if __name__ == '__main__':
    res = Solution()
    print(res.fractionToDecimal(20, 7))