#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 328.py

@time: 2019/5/24 22:17

@desc:

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        o = odd
        e = even
        while e:
            o.next = e.next
            if o.next: # 到了最后，o指向最后一个节点，不再后移，否则指向NULL
                o = o.next
            e.next = o.next
            e = e.next
        o.next = even
        return odd
