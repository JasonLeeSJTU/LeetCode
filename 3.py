#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 3.py

@time: 2019/6/3 17:43

@desc:

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, j = 0, 0
        res = 1
        string = s[0]
        while j < len(s) - 1:
            j += 1
            if s[j] in string:
                id = string.index(s[j])
                string = string[id+1:] + s[j]
                i = i + id + 1
            else:
                string += s[j]

            if j-i+1 > res:
                res = j-i+1

        return res

    def better(self, s):
        if not s:
            return 0
        i = j = 0
        max_len = 1
        dict = {s[i]: i}
        while j < len(s) - 1:
            j += 1
            if s[j] in dict:
                i = max(i, dict[s[j]] + 1) # 这里保证i不会回退到以前的元素位置
            dict[s[j]] = j # 这样可以抵消掉原有的dict中的元素，类似于删除了
            max_len = max(max_len, j-i+1)

        return max_len

    def best(self, s):
        if not s:
            return 0
        string = s[0]
        max_len = 0
        for i in s[1:]:
            if i in string: # 这句速度很快
                id = string.find(i)
                string = string[id+1:]
            string += i
            max_len = max(max_len, len(string))
        return max_len


if __name__ == '__main__':
    res = Solution()
    print(res.better('tmmzuxt'))