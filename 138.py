#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 138.py

@time: 2019/6/3 13:26

@desc:

'''
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        res = Node(head.val, None, None)
        root = res
        dict = {head.val: res}
        while head:
            next = head.next
            rand = head.random
            if next:
                if next.val not in dict:
                    root.next = Node(next.val, None, None)
                    dict[next.val] = root.next
                else:
                    root.next = dict[next.val]
            if rand:
                if rand.val not in dict:
                    root.random = Node(rand.val, None, None)
                    dict[rand.val] = root.random
                else:
                    root.random = dict[rand.val]
            head = next
            root = root.next
        return res

    def better(self, head):
        # 1. 在原始链表的每一个节点后面插入一个新节点
        # 2. 新节点的random指向老节点的random的后一个
        # 3. 将所有新节点提取出来，这里要注意把原来的链表也要恢复
        # 参考网址https://www.cnblogs.com/zuoyuan/p/3745126.html
        if not head:
            return None
        root = head
        while root:
            node = Node(root.val, None, None)
            node.next = root.next
            root.next = node
            root = node.next

        root = head
        while root:
            node = root.next
            if root.random:
                node.random = root.random.next
            root = node.next

        old = head
        new = head.next
        res = new
        while new.next:
            old.next = new.next
            old = old.next
            new.next = old.next
            new = new.next
        # 以下两句很重要，否则old的最后一位指向new的最后一位
        old.next = None
        new.next = None

        return res