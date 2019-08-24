#!usr/bin/env python
#-*- coding:utf-8 -*-

'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M
思路：从右向左依次处理：
当遇到这个字母表示的数字比后一个小的时候，减去这个数；
否则，累加
'''

class Solution:
	def romanToInt(self,s):
		d = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		sum = 0
		for i in range(len(s)-1,-1,-1):
			if(i<len(s)-1) and (d[s[i]] < d[s[i+1]]):
				sum -= d[s[i]]
			else:
				sum += d[s[i]]
		return sum
if __name__ == '__main__':
	x=Solution()
	s='IX'
	print(x.romanToInt(s))


#知识补充：range步长

s='IX'
for i in range(len(s)-1,-1,-1):
	print(i)
