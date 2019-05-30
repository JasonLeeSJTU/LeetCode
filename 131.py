#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 131.py

@time: 2019/5/30 15:30

@desc:

'''
from typing import List
# // DFS - Deepth First Search
# //
# //   For example: "aaba"
# //
# //                     +------+
# //              +------| aaba |-----+
# //              |      +------+     |
# //            +-v-+              +-v--+
# //            | a |aba           | aa |ba
# //        +---+---+--+           +--+-+
# //        |          |              |
# //      +-v-+     +--v--+         +-v-+
# //      | a |ba   | aba |\0       | b |a
# //      +-+-+     +-----+         +-+-+
# //        |        a, aba           |
# //      +-v-+                     +-v-+
# //      | b |a                    | a |\0
# //      +-+-+                     +---+
# //        |                      aa, b, a
# //      +-v-+
# //      | a |\0
# //      +---+
# //    a, a, b, a

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 深度优先搜索
        def dfs(s, path):
            if not s:
                self.res.append(path)
            for i in range(1, len(s) + 1):
                if is_palindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]])

        def is_palindrome(s):
            return s == s[::-1]

        self.res = []
        dfs(s, [])

        return self.res

if __name__ == '__main__':
    s = 'aabaa'
    res = Solution()
    a = res.partition(s)
    print(a)