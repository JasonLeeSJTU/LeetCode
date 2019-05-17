#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 230.py

@time: 2019/5/17 16:47

@desc:

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if k < 1:
            return -1
        if not root:
            return -1

        stack = []
        stack.append(root)
        while root.left:
            root = root.left
            stack.append(root)

        # now root.val is the smallest element
        count = 0
        while stack:
            root = stack.pop()
            count += 1
            if count >= k:
                break

            if root.right:
                root = root.right
                stack.append(root)
                while root.left:
                    root = root.left
                    stack.append(root)

        return root.val