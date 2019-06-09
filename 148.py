#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 148.py

@time: 2019/6/9 15:54

@desc:

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge_sort(self, head):
        if not head or not head.next:
            return []

        # 把链表分成两部分
        prev, fast, slow = None, head, head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None # 阶段左边部分的链表
        left = self.merge_sort(head)
        right = self.merge_sort(slow)
        return self.merge(left, right)

    def merge(self, l1, l2):
        root = p = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return root.next

    def quick_sort(self, head):
        # 把小于base的节点串成一串，大于base的节点串成一串，等于base的节点串成一串
        # 返回一串的开头节点和结尾节点，结尾节点便于连接不同的串
        if not head or not head.next:
            return head, head
        #partition
        base = head
        left, right = ListNode(None), ListNode(None)
        p, b, l, r = head.next, base, left, right
        while p:
            if p.val < base.val:
                l.next = p
                l = l.next
            elif p.val > base.val:
                r.next = p
                r = r.next
            else:
                b.next = p
                b = b.next
            p = p.next
        # 切断联系
        l.next = None
        r.next = None
        b.next = None

        ls, le = self.quick_sort(left.next)
        rs, re = self.quick_sort(right.next)
        # 连接串
        if not ls: # 没有左子串
            ls = base # ls当做合并后的串的开头
        else:
            le.next = base
        if not rs: # 没有右子串
            re = b # re作为合并后的串的结尾
        else:
            b.next = rs
        return ls, re


    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return []
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def partition(num, left, right):
            i, j = left+1, right
            start = right
            while True:
                while i+1 <= right and num[i] <= num[left]:
                    if num[i] == num[left] and start >= i:
                        start = i
                    else:
                        start = right # 确保 j 的左侧，一直到start都是num[left]
                    i += 1
                while j-1 >= left and num[j] > num[left]:
                    j -= 1
                if i >= j:
                    break
                num[i], num[j] = num[j], num[i]
            num[left], num[j] = num[j], num[left]
            if start > j:
                start = j
            return [start, j]

        def quick_sort(num, start, end):
            if start >= end:
                return
            [left, right] = partition(num, start, end)
            quick_sort(num, start, left-1)
            quick_sort(num, right+1, end)

        quick_sort(nums, 0, len(nums)-1)
        root = ListNode(nums[0])
        temp = root
        for i in nums[1:]:
            temp.next = ListNode(i)
            temp = temp.next

        return root

if __name__ == '__main__':
    res = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    # a = res.sortList(head)
    a, b = res.quick_sort(head)
    print(a)