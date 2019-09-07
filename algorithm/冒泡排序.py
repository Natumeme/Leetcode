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
1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
3.重复第二部，直到所有元素均排序完毕
'''