#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 1049.py

@time: 2019/5/19 11:49

@desc:

'''

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        all = sum(stones)
        for a in stones:
            dp |= {a + i for i in dp}
        # 循环结束之后，dp中包含了所有元素的和，包括任意0个元素和、任意1个元素和、任意2个元素和、任意3个元素和，等等。最大元素是所有元素和，即all
        # 对于dp中的任意一个元素i，(all - i, i)把stones中的所有元素分成了两堆，all - i - i就是两堆的差
        return min(abs(all - i - i) for i in dp)

    def lastStoneWeightII1(self, stones: List[int]) -> int:
        dp = {0}
        for a in stones:
            dp = {a + i for i in dp} | {a - i for i in dp}

        return min(abs(i) for i in dp)


if __name__ == '__main__':
    res = Solution()
    a = res.lastStoneWeightII1([2, 7, 4, 1, 8, 1])
    print(a)
