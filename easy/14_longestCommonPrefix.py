#!usr/bin/env python
#-*- coding:utf-8 -*-


'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
输入: ["flower","flow","flight"]
输出: "fl"

思路
第一步：找出长度最短的字符串；
第二步：依次与长度最短的字符串比较
'''


#方法一
class Solution:
	def longestCommonPrefix(self,strs):
		if len(strs) == 0:
			return ""
		minlen = min([len(x) for x in strs])
		end = 0
		while end < minlen:
			for i in range(1,len(strs)):
				if strs[i][end] != strs[i-1][end]:
					return strs[0][:end]
			end += 1
		return strs[0][:end]

if __name__ == '__main__':
	s=Solution()
	strs=["flower","flow","flight"]
	print(s.longestCommonPrefix(strs))

#方法二
class Solution(object):
	def longestCommonPrefix(self,strs):
		#判断是否为空
		if not strs:
			return ''
		#当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最小的字符串
		s1=min(strs)

		# 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最大的字符串
		s2=max(strs)

		# 使用枚举变量s1字符串的每个字母和下标
		for i ,c in enumerate(s1):
			if c != s2[i]:
				return s1[:i]
		return s1
if __name__ == '__main__':
	s=Solution()
	strs=["flower","flow","flight"]
	print(s.longestCommonPrefix(strs))

