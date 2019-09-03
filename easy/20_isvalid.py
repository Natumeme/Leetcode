#!usr/bin/env python
#-*- coding:utf-8 -*-


'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
'''
class Solution:
	def isValid(self,s):
		sta=[None]
		dic={")":"(","}":"{","]":"["}
		for t in s:
			if(t in dic and dic[t]==sta[len(sta)-1]):
				sta.pop()
			else:
				sta.append(t)
		return len(sta)==1
if __name__=='__main__':
	x=Solution()
	s="()"
	print(x.isValid(s))


'''
知识补充：
栈的作用
1.内栈管理中使用的堆栈
2.基于栈实现的二叉树的遍历
3.在处理需求中的平衡问题：
 a.判断符号是成堆出现的，比如（）
 b.判断这个字符串是否是回文字符串
'''