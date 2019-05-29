#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 279.py

@time: 2019/5/28 16:13

@desc:

'''
class Solution:
    def numSquares(self, n: int) -> int:
        # 动态规划
        # f(n) = min{f(n-j^2) + 1}，其中j取值1,2,...,int(sqrt(n))
        f = [0x7fffffff for i in range(n+1)]
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            j = 1
            while j*j <= i:
                f[i] = min(f[i], f[i-j*j]+1) # 由于f[0]=0，这里当i==j*j时，就是n本身，也即f[n] = 1
                j += 1
        return f[-1]

class StaticDP:
    # 静态存储dp，减少计算量
    dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self.dp
        m = len(dp)
        for i in range(m, n+1):
            dp += [min(dp[i-j*j] for j in range(1, int(i**0.5) + 1)) + 1]
        return dp[n] # 这里不能用dp[-1]，因为上一次调用可能是n=10，这一次调用是n=2，直接返回值即可。dp[-1]是dp[10]的结果，是错的

class BFS:
    # 广度优先搜索，找到最短路径
    # 一层一层遍历树结构，
    def numSquares(self, n: int) -> int:
        # 根据n值，找到比n小的所有平方数
        i = 1
        squares = []
        while i*i <= n:
            squares.append(i*i)
            i += 1
        num = [n] # 下一层是num中的数，减去squares的所有数
        count = 0
        while num:
            temp = []
            count += 1
            for i in num:
                for j in squares:
                    if i - j < 0: # 节点不能为负
                        break
                    elif i == j:
                        return count # 找到了最短路径，因为是一层一层遍历的，所以这个count肯定是最短路径
                    else:
                        temp.append(i-j)
            num = set(temp)

if __name__ == '__main__':
    res = BFS()
    print(res.numSquares(8504))