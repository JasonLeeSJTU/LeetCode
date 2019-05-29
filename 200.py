#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 200.py

@time: 2019/5/29 22:47

@desc:

'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 遇到一个1，就递归地把与这个位置四联通的所有1下沉为0。
        # 递归的方式可以保证所有联通的1全部下沉为0
        # 递归结束，岛的数量加1
        def sink(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == '0':
                return 0
            # 下沉为0
            grid[i][j] = '0'
            sink(i-1, j)
            sink(i+1, j)
            sink(i, j-1)
            sink(i, j+1)
            return 1

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num += sink(i,j)

        return num

if __name__ == '__main__':
    # grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    # grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    # grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    res = Solution()
    a = res.numIslands(grid)
    print(a)