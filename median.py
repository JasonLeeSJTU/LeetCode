#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: median.py

@time: 2019/6/15 14:18

@desc:

'''

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m == 0 and n == 0:
            return 0.0

        total = m + n
        if total % 2 == 1:
            return self.kth_largest(A, B, total // 2 + 1) * 1.0
        else:
            # a = self.kth_largest(A, B, total // 2)
            # b = self.kth_largest(A, B, total // 2 + 1)
            a, b = self.kth_largest_two(A, B, total // 2)
            return (a + b) / 2.0

    def kth_largest(self, A, B, kth):
        m, n = len(A), len(B)
        if m == 0:
            return B[kth-1]
        if n == 0:
            return A[kth-1]
        if kth == 1:
            return min(A[0], B[0])

        mid = kth // 2
        a, b = float("inf"), float("inf")
        if m >= mid:
            a = A[mid - 1]
        if n >= mid:
            b = B[mid - 1]
        if a < b:
            return self.kth_largest(A[mid:], B, kth - mid)
        else:
            return self.kth_largest(A, B[mid:], kth - mid)

    def kth_largest_two(self, A, B, kth):
        m, n = len(A), len(B)
        if m == 0:
            return B[kth-1], B[kth]
        if n == 0:
            return A[kth-1], A[kth]
        if kth == 1:
            if A[0] <= B[0]:
                a = A[0]
                b = min(A[1], B[0]) if m >= 2 else B[0]
            else:
                a = B[0]
                b = min(A[0], B[1]) if n >= 2 else A[0]
            return a, b


        mid = kth // 2
        a, b = float("inf"), float("inf")
        if m >= mid:
            a = A[mid - 1]
        if n >= mid:
            b = B[mid - 1]
        if a < b:
            return self.kth_largest_two(A[mid:], B, kth - mid)
        else:
            return self.kth_largest_two(A, B[mid:], kth - mid)

if __name__ == '__main__':
    a = [1,2,3]
    b = [4,5,6,7,8,9,10,11,12,13,14,15,16]
    res = Solution()
    c = res.findMedianSortedArrays(a, b)
    print(c)