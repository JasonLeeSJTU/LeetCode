#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 103.py

@time: 2019/5/29 21:16

@desc:

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        count = 1 # 标记压入节点的顺序，先左，还是先右
        while stack:
            temp = []
            ts = []
            while stack:
                node = stack.pop()
                temp.append(node.val)
                if count & 1: # 单数层, the same with count % 2
                    if node.left:
                        ts.append(node.left)
                    if node.right:
                        ts.append(node.right)
                else:
                    if node.right:
                        ts.append(node.right)
                    if node.left:
                        ts.append(node.left)
            stack = ts
            count += 1
            res.append(temp)

        return res

    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        left_stack = [root]
        right_stack = []
        res = []
        while left_stack or right_stack:
            temp = []
            while left_stack:
                node = left_stack.pop()
                temp.append(node.val)
                if node.left:
                    right_stack.append(node.left)
                if node.right:
                    right_stack.append(node.right)
            if temp:
                res.append(temp)

            temp = []
            while right_stack:
                node = right_stack.pop()
                temp.append(node.val)
                if node.right:
                    left_stack.append(node.right)
                if node.left:
                    left_stack.append(node.left)
            if temp:
                res.append(temp)

        return res