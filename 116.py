#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 116.py

@time: 2019/6/10 15:58

@desc:

'''
import collections
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = collections.deque()
            previous = None
            while queue:
                node = queue.pop()
                node.next = previous
                previous = node
                if node.left:
                    temp.appendleft(node.right)
                    temp.appendleft(node.left)
            queue = temp
        return root


    def better(self, root):
        # real O(1) space
        if not root:
            return root
        temp = root
        while root:
            next = root.left
            while root and root.left:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                root = root.next
            root = next
        return temp