#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 347.py

@time: 2019/5/17 11:46

@desc:

'''
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 1:
            return []
        freq = {}
        for i in nums:
            if i not in freq.keys():
                freq[i] = 1
            else:
                freq[i] += 1

        # 从数组中找到k个最大的数
        res = []
        count = 0
        for i in freq:
            if count < k:
                res.append(i)
                count += 1
                continue
            res = sorted(res, key=freq.get)
            if freq[i] > freq[res[0]]: # 大于最小值，加入进来
                res.pop(0)
                res.append(i)

        return res

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)

if __name__ == '__main__':
    res = Solution()
    arr = [4,1,-1,2,-1,2,3]
    a = res.topKFrequent1(arr, 2)
    print(a)