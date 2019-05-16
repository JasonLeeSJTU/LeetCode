#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 94.py

@time: 2019/5/16 21:48

@desc:

'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: list):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
