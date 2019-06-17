#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 114.py

@time: 2019/6/18 0:37

@desc:

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        dummy = head = TreeNode(None)
        stack = [root]
        while stack:
            node = stack.pop()
            head.right = node
            head = head.right
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node.left)
                node.left = None
        root = dummy.right

    def recursive(self, root):
        if not root:
            return
        self.prev = root # prev的值一直在变
        # 展平左子树
        self.recursive(root.left) # 这个函数结束后，prev变成了最后一个节点

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        # 展平右子树
        self.recursive(root.right)