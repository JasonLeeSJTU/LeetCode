#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 287.py

@time: 2019/5/24 0:27

@desc:

'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 当做链表中去找环，环的入口节点就是
        p1 = nums[0]
        p2 = nums[0]
        while True:
            p1 = nums[p1]  # 每次走一步
            p2 = nums[p2]
            p2 = nums[p2]  # 每次走两步
            if p1 == p2:
                break
        # p1 从头开始，p2从相遇的节点开始，每次都移动一步，两者相遇在环的入口节点
        p1 = nums[0]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1


if __name__ == '__main__':
    a = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    res = Solution()
    b = res.findDuplicate(a)
    print(b)
