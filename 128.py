#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 128.py

@time: 2019/6/17 11:42

@desc:

'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        data = set(nums)
        max_count = 1
        for i in nums:
            if i not in data:
                continue
            count = 1
            data.remove(i)
            j = i
            while j - 1 in data:
                count += 1
                data.remove(j-1)
                j -= 1
            j = i
            while j + 1 in data:
                count += 1
                data.remove(j+1)
                j += 1
            max_count = max(max_count, count)
        return max_count

    def better(self, nums):
        if not nums:
            return 0
        data = set(nums)
        count = 1
        for i in data:
            if i-1 not in data:
                j = i + 1
                while j in data:
                    j += 1
                count = max(count, j - i)
        return count

if __name__ == '__main__':
    res = Solution()
    nums = [100,4,200,1,3,2]
    a = res.longestConsecutive(nums)
    b = res.better(nums)
    print(a)
    print(b)

