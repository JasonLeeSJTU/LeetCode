#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 227.py

@time: 2019/6/8 17:11

@desc:

'''
import collections
class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque()
        i = 0
        while i < len(s):
            if s[i] == ' ':
                pass
            elif s[i] in '+-':
                stack.append(s[i])
            elif s[i] in '*/':
                x = s[i]
                a = stack.pop()
                string = s[i+1]
                i += 1
                while i+1 < len(s) and s[i+1] not in '+-*/': # 多位整数
                    string += s[i+1]
                    i += 1
                b = int(string)
                c = a*b if x == '*' else int(a/b)
                stack.append(c)
            else:
                string = s[i]
                while i+1 < len(s) and s[i+1] not in ' +-*/': #多位整数
                    i += 1
                    string += s[i]
                stack.append(int(string))
            i += 1

        while len(stack) > 1: # len == 1时就是最后的结果
            a = stack.popleft()
            x = stack.popleft()
            b = stack.popleft()
            c = a + b if x == '+' else a - b
            stack.appendleft(c)

        return stack.pop()

    def better(self, s):
        stack = []
        num = 0
        preOp = '+'
        for id, i in enumerate(s):
            if i not in ' +-*/':
                num = num*10 + int(i)
            if i in '+-*/' or id == len(s) - 1:
                if preOp == '+':
                    stack.append(num)
                elif preOp == '-':
                    stack.append(-num)
                elif preOp == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preOp = i
                num = 0
        return sum(stack)

    def best(self, s):
        s += '+' #添加结尾标记
        sum, num, last, preOp = 0, 0, 0, '+'
        for i in s:
            if i not in ' +-*/':
                num = num*10 + int(i)
                continue
            if i != ' ':
                if preOp == '+':
                    sum += last
                    last = num
                elif preOp == '-':
                    sum += last
                    last = -num
                elif preOp == '*':
                    last = last * num
                else:
                    last = int(last / num)
                preOp = i
                num = 0
        return sum + last


if __name__ == '__main__':
    res = Solution()
    s = "1*2-3*3"
    a = res.calculate(s)
    print(a)
    print(res.better(s))
    print(res.best(s))