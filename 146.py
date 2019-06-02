#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 146.py

@time: 2019/6/2 16:42

@desc:

'''
import collections
# 使用双向链表使得删除操作复杂度是O(1)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = collections.defaultdict()
        self.capacity = capacity
        self.len = 0 # current length
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.dict:
            node = self._remove(key)
            self._add(node)
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.dict: # 对于重复的key，删除原有的
            self._remove(key)
            self.dict[key] = node
            self._add(node)
            return

        if self.len >= self.capacity: # 超过了容量限制，删除最左边的节点
            temp = self.head.next
            self._remove(temp.key)
            del self.dict[temp.key]
            self.len -= 1

        self._add(node)
        self.dict[key] = node
        self.len += 1

    def _remove(self, key):
        node = self.dict[key]
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        return node

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node


if __name__ == '__main__':
    res = LRUCache(2)
    res.put(1, 1)
    res.put(2, 2)
    print(res.get(1))
    res.put(3, 3)
    print(res.get(2))
    res.put(4, 4)
    print(res.get(1))
    print(res.get(3))
    print(res.get(4))
