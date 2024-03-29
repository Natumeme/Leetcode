#!usr/bin/env python
#-*- coding:utf-8 -*-

def bubbleSort(arr):
	for i in range(1,len(arr)):
		for j in range(0,len(arr)-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr
arr=[3,2,8,7,5,0,4]
print(bubbleSort(arr))

'''
思路：
1。比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2。对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。这步做完，最后的元素会是最大的数。
3。针对所有的元素重复以上的步骤，除了最后一个。
4。持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''