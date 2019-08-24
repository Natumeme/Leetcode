#!/usr/bin/env python
#-*-coding:utf-8-*-


class Solution:
	def twoSum(self,nums,target):
		dic=dict()
		for index,value in enumerate(nums):
			sub=target-nums[index]
			if sub in dic:
				return dic[sub],index
			else:
				dic[value]=index

if __name__ == '__main__':
	s=Solution()
	nums = [2, 7, 11, 15]
	target=9
	print(s.twoSum(nums,target))


