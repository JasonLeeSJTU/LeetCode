#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 384.py

@time: 2019/5/22 21:42

@desc:

'''


class Solution:

    def __init__(self, nums: List[int]):
        self.list = nums
        self.nums = list(nums) # 深拷贝

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.list

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = []
        temp = self.list
        for i in range(len(self.list)):
            x, id = self.helper(temp)
            res.append(x)
            temp = temp[:x] + temp[x+1:]
        return res


    def helper(self, nums):
        import random
        idx = random.randint(0, len(nums)-1)
        return nums[idx], idx

    def better_shuffle(self):
        import random
        res = self.list # 这里是浅拷贝，reset函数不能输出正确的值，需要记录一个额外的nums变量
        for i in range(len(self.list)):
            id = random.randrange(i, len(self.list))
            res[i], res[id] = res[id], res[i]
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
