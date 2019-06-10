#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 208.py

@time: 2019/6/10 16:33

@desc:

'''

class Node:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for i, v in enumerate(word):
            if v not in root.child:
                root.child[v] = Node()
            root = root.child[v]
        root.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for i in word:
            if i not in root.child:
                return False
            root = root.child[i]
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for i in prefix:
            if i not in root.child:
                return False
            root = root.child[i]
        return True

if __name__ == '__main__':
    res = Trie()
    res.insert('apple')
    a = res.search('apple')
    print(a)