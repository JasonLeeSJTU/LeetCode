#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 49.py

@time: 2019/5/26 15:12

@desc:

'''
from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        #f = {}
        f = collections.defaultdict(list)
        for i in strs:
            j = ''.join(sorted(i))
            if j not in f.keys():
                f[j] = [i]
            else:
                f[j] += [i]

        # res = []
        # for i in f:
        #     res.append(f[i])
        return list(f.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution()
    a = res.groupAnagrams(strs)
    print(a)
