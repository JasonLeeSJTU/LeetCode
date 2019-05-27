#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 11.py

@time: 2019/5/27 13:35

@desc:

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # f(n) = max{f(n-1), max[min(ai, an)*(n-i)]}
        f = [0 for i in range(len(height))]
        f[1] = min(height[0], height[1]) * 1
        for i in range(2, len(height)):
            # get max{min(aj,ai)*(i-j)}
            max_w = 0
            for j in range(i):
                temp = min(height[j], height[i]) * (i - j)
                if temp > max_w:
                    max_w = temp

            f[i] = max(f[i-1], max_w)

        return f[-1]

    def better(self, height):
        # 对于开头和结果的两个点i, j。如果i<j，则以i为边界能得到的最大值就是i~j区间。
        # 因此，使i++，即不再考虑以i为边界的情况。
        # 若i>j，则以j为边界能得到的最大值就是i~j区间，使j--，即不再考虑以j为边界的情况。
        # 若i==j，则同时满足以上两种情况。
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

    def best(self, height):
        # 跟上面的better方法一样，只是进一步做了优化：
        # 1. i<j时，增大i的时候j-i变小了，因此需要一直增大i，直到height[i]比原本的值大，才有可能得到新的最大值
        # 2. 同上，减小j的时候j-i也变小了，因此需要一直减小j，直到height[j]比原本的值大才行。
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            area = 0
            if height[i] < height[j]:
                area = height[i] * (j - i)
                temp = height[i]
                while height[i] <= temp: # 这里i的值不会超过j
                    i += 1
            else:
                area = height[j] * (j - i)
                temp = height[j]
                while height[j] <= temp and j: # 防止j<0
                    j -= 1
            water = area if area > water else water
        return water