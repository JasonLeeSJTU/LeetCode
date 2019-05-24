#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 378_binarySearch.py

@time: 2019/5/24 20:40

@desc:

'''
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (right + left) // 2
            # 统计所有小于mid的元素的数量
            col = cols - 1
            count = 0
            for row in range(rows):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += col + 1

            if count >= k:
                right = mid
            elif count < k:
                left = mid + 1

        return left

if __name__ == '__main__':
    a = [[1,5,9],[10,11,13],[12,13,15]]
    res = Solution()
    b = res.kthSmallest(a, 8)
    print(b)