#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 98.py

@time: 2019/6/2 17:36

@desc:

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历，得到的数组应该是从小到大排序的
        # 不要用递归，用循环可以迅速判断相邻的两个元素是否符合要求
        stack = []
        x = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < x:
                return False
            else:
                x = root.val
            root = root.right
        return True

if __name__ == '__main__':
    a = float('-inf')
    print(a)