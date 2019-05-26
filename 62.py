#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 62.py

@time: 2019/5/26 14:20

@desc:

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 从(0,0)走到(m-1, n-1)一共有m+n-2步，其中m-1向下，n-1向右。
        # 从m+n-2步中，选取m-1步向下走即可。
        # 结果就是Combination(m+n-2, m-1)
        import math
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

    def dp(self, m, n):
        # 动态规划
        f = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]

        return f[-1][-1]

if __name__ == '__main__':
    res = Solution()
    a = res.uniquePaths(23, 12)
    b = res.dp(23,12)
    print(a)
    print(b)