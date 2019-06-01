#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 127.py

@time: 2019/6/1 20:24

@desc:

'''
from typing import List
import collections
import re
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = collections.deque()
        queue.append(beginWord)
        count = 1
        while queue:
            temp = collections.deque()
            flag = False # 标记是否找到了下一步
            while queue:
                word = queue.popleft()
                for i in range(len(word)):
                    if not wordList:
                        return 0 # There is no possible transform

                    record = []
                    for j in wordList:
                        if re.search(word[:i] + '[a-z]' + word[i+1:], j):
                            if j == endWord:
                                count += 1
                                return count
                            temp.append(j)
                            # wordList.remove(j) # remove 会改变索引，导致38行循环跳过某些元素
                            record.append(j)
                            flag = True
                    for j in record:
                        wordList.remove(j)
            if not flag:
                return 0 # 无法进行下一步，不存在
            queue = temp
            count += 1

        return count

if __name__ == '__main__':
    res = Solution()
    list = ["hot","dot","dog"]
    print(res.ladderLength("hot", "dot", list))
