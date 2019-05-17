#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 78_1.py

@time: 2019/5/17 16:41

@desc:

'''
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [j + [i] for j in res]
        return res

if __name__ == '__main__':
    res = Solution()
    a = res.subsets([1,2,3])
    print(a)