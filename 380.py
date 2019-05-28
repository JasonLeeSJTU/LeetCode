#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 380.py

@time: 2019/5/28 13:53

@desc:

'''
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos.keys():
            self.data.append(val)
            self.pos[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos.keys():
            # 把要移除的元素移动到两个数组的末尾，这样pos中的其他位置的索引不会受到影响
            idx, last = self.pos[val], self.data[-1]
            self.data[idx] = last
            self.pos[last] = idx
            self.data.pop()
            self.pos.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data[random.randint(0, len(self.data) - 1)]

if __name__ == '__main__':
    res = RandomizedSet()
    print(res.insert(3))
    print(res.insert(-2))
    print(res.remove(2))
    print(res.insert(1))
    print(res.insert(-3))
    print(res.insert(-2))
    print(res.remove(-2))
    print(res.remove(3))
    print(res.insert(-1))
    print(res.remove(-3))
    print(res.insert(1))
    print(res.insert(-2))
    print(res.insert(-2))
    print(res.insert(-2))
    print(res.insert(1))
    print(res.getRandom())
    print(res.insert(-2))
    print(res.remove(0))
    print(res.insert(-3))
    print(res.insert(1))
