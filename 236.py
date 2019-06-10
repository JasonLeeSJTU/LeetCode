#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 236.py

@time: 2019/6/10 13:15

@desc:

'''
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.f = collections.defaultdict(set)
        self.res = None
        def dp(root, p, q):
            if self.res:
                return
            if root.val == p.val:
                self.f[root].add(p)
            if root.val == q.val:
                self.f[root].add(q)
            if root.left:
                dp(root.left, p, q)
                self.f[root] |= self.f[root.left]
            if root.right:
                dp(root.right, p, q)
                self.f[root] |= self.f[root.right]
            if p in self.f[root] and q in self.f[root]:
                if not self.res:
                    self.res = root


        dp(root, p, q)
        return self.res

    def better(self, root, p, q):
        # 遍历，保存每个节点的父节点
        parent = {root: None}
        stack = [root]
        # 循环，一直到p和q都访问到
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # 把p的所有祖先节点存储到一个set里面
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]

        # q 和p的第一个公共祖先节点，就是LCA
        while q not in ancestor:
            q = parent[q]

        return q


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    res = Solution()
    a = res.lowestCommonAncestor(root, TreeNode(5), TreeNode(4))