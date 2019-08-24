#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

#解法一
#解题思路：用字典模拟哈希求解，把索引序列添加到字典里["value":"index"]
class Solution():
	def twoSum(self,nums,target):
		dic = dict()
		for index,value in enumerate(nums):
			sub = target - value
			if sub in dic:
				return dic[sub],index
			else:
				dic[value]=index
if __name__ == '__main__':
	nums = [2, 11, 7, 15]
	target = 9
	s = Solution()
	print(s.twoSum(nums,target))

'''
补充知识点
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
同时列出数据和数据下标，一般用在 for 循环当中
'''

#对一个列表，既要遍历索引又要遍历元素时
#方法一,使用for循环
seq1 = ['one','two','three']
for i in range(len(seq1)):
	print(i,seq1[1])

#方法二，使用enumerate
seq = ['one','two','three']
for i,element in enumerate(seq):
	print(i,element)


#要统计文件的行数
#文件大时比较缓慢
count1 = len(open(filepath,'r').readlines())

#使用enumerate()
count = 0
for index,line in enumerate(open(filepath,'r')):
	count+=1