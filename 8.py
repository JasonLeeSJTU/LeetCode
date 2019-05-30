#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 8.py

@time: 2019/5/30 22:49

@desc:

'''
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        map = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

        negative = False
        start = 0
        for id, i in enumerate(str):
            if i != ' ':
                if i == '+':
                    negative = False
                    if id + 1 < len(str) and str[id + 1] in map.keys():
                        start = id + 1
                        break
                    else:
                        return 0
                elif i == '-':
                    negative = True
                    if id + 1 < len(str) and str[id + 1] in map.keys():
                        start = id + 1
                        break
                    else:
                        return 0
                elif i in map.keys():
                    start = id
                    break
                else:
                    return 0

        num = 0
        for i in range(start, len(str)):
            if str[i] in map.keys():
                num = num*10 + int(str[i])
                if not negative:
                    if num > 0x7fffffff:
                        return 0x7fffffff
                else:
                    if num > 0x80000000:
                        return -0x80000000
            else:
                break

        return num if not negative else -num

if __name__ == '__main__':
    res = Solution()
    a = res.myAtoi("  -42")
    print(a)