#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 230_recursive.py

@time: 2019/5/17 17:06

@desc:

'''

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if k < 1 or not root:
            return -1

        return self.helper(root)[k-1]

    def helper(self, root):
        if not root:
            return []   # 这里只有返回[] 下面的结果才能相加

        return self.helper(root.left) + [root.val] + self.helper(root.right)
