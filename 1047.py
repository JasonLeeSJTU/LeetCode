#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 1047.py

@time: 2019/5/19 10:41

@desc:

'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) <= 1:
            return S
        temp = list(S)
        flag = False
        i = 0
        while len(temp) > 1 and i < len(temp) - 1:
            if temp[i] == temp[i+1]:
                temp.pop(i)
                temp.pop(i) # this is the previous i+1 item
                if i != 0:
                    i -= 1  # you only need to go back one char to double check if new dup appears.
            else:
                i += 1

        return ''.join(temp)

    def removeDuplicates1(self, S: str) -> str:
        if len(S) <= 1:
            return S
        res = []
        for i in S:
            if res and i == res[-1]:
                res.pop()
            else:
                res.append(i)
        return ''.join(res)


if __name__ == '__main__':
    res = Solution()
    a = res.removeDuplicates1('azxxzy')
    print(a)