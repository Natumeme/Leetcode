#!usr/bin/env python
#-*- coding:utf-8 -*-


'''
判断一个整数是否是回文数。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
输入: 121
输出: true
'''

class Solution:
	def isPalindrome(self,x):
		if(x>=0):
			if(x==int(str(x)[::-1])):
				return True
			else:
				return False
		return False
if __name__ == '__main__':
	s=Solution()
	x=9999
	print(s.isPalindrome(x))