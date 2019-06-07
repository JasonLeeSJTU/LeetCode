#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 150.py

@time: 2019/6/7 16:59

@desc:

'''
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in oper:
                stack.append(int(i))
            else:
                first, second = stack.pop(), stack.pop()
                if i == '+':
                    res = second + first
                elif i == '-':
                    res = second - first
                elif i == '*':
                    res = second * first
                else:
                    res = int(second/first) # 1//(-2)=-1，不符合题目要求。
                stack.append(res)
        return stack.pop()

if __name__ == '__main__':
    res = Solution()
    # ar = ["2","1","+","3","*"]
    # ar = ["4", "13", "5", "/", "+"]
    ar = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    a = res.evalRPN(ar)
    print(a)
