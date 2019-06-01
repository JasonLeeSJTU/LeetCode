#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 127_bfs_bidirection.py

@time: 2019/6/1 21:54

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

        queue_begin = collections.deque()
        queue_end = collections.deque()
        queue_begin.append((beginWord, 1))
        queue_end.append((endWord, 1))
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        while queue_begin and queue_end:
            flag = self.is_visited(queue_begin, visited_begin, visited_end, dict)
            if flag:
                return flag
            flag = self.is_visited(queue_end, visited_end, visited_begin, dict)
            if flag:
                return flag
        return 0

    def is_visited(self, queue, visited_me, visited_other, dict):
        word, level = queue.popleft()
        for i in range(len(word)):
            mask = word[:i] + '*' + word[i+1:]
            for j in dict[mask]:
                if j in visited_other:
                    return level + visited_other[j]
                if j not in visited_me:
                    visited_me[j] = level + 1
                    queue.append((j, level + 1))
        return False # 没有找到相遇节点


if __name__ == '__main__':
    res = Solution()
    dict = ["a", "b", "c"]
    print(res.ladderLength("a", "c", dict))
