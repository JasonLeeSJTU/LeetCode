#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 454.py

@time: 2019/5/19 10:03

@desc:

'''
from typing import List
import collections


class Solution:
    # 时间复杂度 O(n^4)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = []
        count = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    for l in range(len(D)):
                        if A[i] + B[j] + C[k] + D[l] == 0:
                            res.append((i, j, k, l))
                            count += 1
        return count

    # 时间复杂度 O(n^2)
    def better(self, A, B, C, D):
        s = collections.Counter(-i - j for i in A for j in B)
        return sum(s[k + l] for k in C for l in D)


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    res = Solution()
    # a = res.fourSumCount(A, B, C, D)
    a = res.better(A, B, C, D)
    print(a)
