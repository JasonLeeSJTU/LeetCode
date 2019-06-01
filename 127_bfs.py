#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 127_bfs.py

@time: 2019/6/1 21:32

@desc:

'''
from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        # 对字典中的字符串进行预处理，使得'hot', 'hit'归入'h*t'，加快访问速度
        dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                dict[word[:i]+'*'+word[i+1:]].append(word)

        queue = collections.deque()
        queue.append((beginWord, 1))
        visited = {}
        while queue:
            word, level = queue.popleft()
            for i in range(len(word)):
                mask = word[:i]+'*'+word[i+1:]
                for j in dict[mask]:
                    if j == endWord:
                        return level + 1
                    if j not in visited: # 避免出现环
                        queue.append((j, level+1))
                        visited[j] = True
                dict[mask] = []
        return 0

if __name__ == '__main__':
    res = Solution()
    dict = ["hot","dot","dog"]
    print(res.ladderLength("hot", "dot", dict))
