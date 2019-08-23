#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
输入: 123
输出: 321
'''

'''
思路：先考虑正负，转换成数组进行切片，最后在判断转换后的数字是否超出范围
'''

class Solution:
	def reverse(self,x):
		if x<0:
			y=int(str(-x)[::-1])
		else:
			y=int(str(x)[::-1])
		if x > 2147483648 or x < -2147483648:
			y = 0
		return y
if __name__ == '__main__':
	x=233
	s=Solution()
	print(s.reverse(x))



