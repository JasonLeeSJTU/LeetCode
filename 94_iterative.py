#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 94_iterative.py

@time: 2019/5/16 22:12

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
        stack = [root]
        # push all the left tree nodes
        while stack[-1].left:
            stack.append(stack[-1].left)

        while stack:
            temp = stack.pop()
            res.append(temp.val)
            # if temp has right child node, push it into the stack
            if temp.right:
                stack.append(temp.right)
                # push all the left tree nodes
                while stack[-1].left:
                    stack.append(stack[-1].left)

        return res