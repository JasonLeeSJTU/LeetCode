#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 19.py

@time: 2019/6/8 23:55

@desc:

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针i，j。j先走n步，i再走。当j到达末尾是，i的下一个节点就是要删除的那个
        i, j = head, head
        for x in range(n):
            j = j.next
        if not j: # 说明要删除的是第一个节点head
            head = head.next
            return head
        while j.next: # j到达最后一个节点
            i = i.next
            j = j.next
        i.next = i.next.next
        return head