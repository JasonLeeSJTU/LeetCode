#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 105.py

@time: 2019/5/30 13:20

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归实现
        # preorder第一个是根节点，inorder中根节点前面的是左子树，后面的是右子树
        if not preorder:
            return
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        id = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:id+1], inorder[:id])
        root.right = self.buildTree(preorder[id+1:], inorder[id+1:])
        return root

    def better(self, preorder, inorder):
        # 使用dict加速
        if not preorder:
            return
        idx = {val: i for i, val in enumerate(inorder)}

        # preorder中的每一个元素都要作为根节点，遍历一遍。
        self.root_idx = 0

        def helper(left, right):
            if left > right:
                return
            root = TreeNode(preorder[self.root_idx])
            self.root_idx += 1
            id = idx[root.val]
            root.left = helper(left, id - 1)
            root.right = helper(id + 1, right)
            return root

        return helper(0, len(preorder) - 1)

if __name__ == '__main__':
    pre = [3,9,20,15,7]
    ino = [9,3,15,20,7]
    res = Solution()
    a = res.better(pre, ino)
    print(a)