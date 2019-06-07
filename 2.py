#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 2.py

@time: 2019/6/5 17:36

@desc:

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ''
        carry = ''
        while l1 and l2:
            temp = l1.val + l2.val
            if temp >= 10:
                sum += str(temp - 10)
                carry += str(1)
            else:
                sum += str(temp)
                carry += str(0)
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum += str(l1.val)
            l1 = l1.next
        while l2:
            sum += str(l2.val)
            l2 = l2.next

        sum = int(''.join(sum[::-1]))
        carry = int(''.join(carry[::-1])) * 10
        sum += carry

        sum = str(sum)[::-1]
        head = ListNode(int(sum[0]))
        temp = head
        for i in range(1, len(sum)):
            temp.next = ListNode(int(sum[i]))
            temp = temp.next

        return head

    def better(self, l1, l2):
        head = l3 = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            sum = a + b + carry
            l3.next = ListNode(sum % 10)
            carry = 1 if sum >= 10 else 0
            l3 = l3.next
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    res = Solution()
    a = res.addTwoNumbers(l1, l2)
    print(a)
