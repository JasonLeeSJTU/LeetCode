#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 142.py

@time: 2019/6/17 17:37

@desc:

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        i, j = head, head
        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                break
        else:
            return None

        i = head
        while i!=j:
            i = i.next
            j = j.next
        return i
