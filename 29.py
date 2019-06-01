#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: 29.py

@time: 2019/5/31 23:57

@desc:

'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 使用位运算进行除法运算
        # 商 = 被除数 - 除数，直到差<除数时，减法的次数
        # 余数 = 减完剩下的
        # 加速方法：每次让被除数-除数的2^n倍，n取值范围：31, 30, 29, ..., 0

        # 需要实现加法和减法，因为还有可能遇到负数，所以还需要求负函数（即绝对值）
        a = dividend if dividend > 0 else self.neg(dividend)
        b = divisor if divisor > 0 else self.neg(divisor)
        quotient, remainder = 0, 0
        for i in range(31, -1, -1):
            # a/2^n >= b 等价于 a >= b*2^n
            if (a >> i) >= b:
                a = self.sub(a, b << i)
                quotient = self.add(quotient, 1 << i)
        if (dividend ^ divisor) < 0: # 两者异号
            quotient = self.neg(quotient)
        if divisor < 0x7fffffff:
            remainder = a
        else:
            remainder = self.neg(a)

        return quotient

    # 加法
    def add(self, a, b):
        while b:
            sum = a ^ b
            carry = a & b
            b = (carry << 1) & 0xffffffff   # 把数据的长度限制在32位，防止python溢出
            a = sum & 0xffffffff
        return a if a < 0x7fffffff else ~(a^0xffffffff)

    # a, b都是正数的减法
    # a - b = a + (-b)
    def sub(self, a, b):
        return self.add(a, self.neg(b))

    # 求负
    def neg(self, a):
        # ~a = -a-1
        return self.add(~a, 1)

if __name__ == '__main__':
    res = Solution()
    print(res.divide(-2, -1))
    print(res.neg(-3))
    print(res.neg(-214))
    print(7 // (-3))
