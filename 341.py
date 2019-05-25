#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 341.py

@time: 2019/5/25 21:27

@desc:

'''


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # flat = lambda x: [j for i in x for j in flat(i)] if isinstance(x, list) else [x]
        def flat(nestedList):
            for i in nestedList:
                if isinstance(i, list):
                    yield from flat(i)
                else:
                    yield i

        self.list = list(flat(nestedList))
        self.count = 0
        self.flag = True

    def next(self):
        """
        :rtype: int
        """
        res = self.list[self.count]
        self.count += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count >= len(self.list):
            self.flag = False

        return self.flag

if __name__ == '__main__':
    nested = [[1,1],2,[1,1]]
    i, v = NestedIterator(nested), []
    while i.hasNext(): v.append(i.next())
    print(v)