#!usr/bin/env python
#-*- coding:utf-8 -*-

'''
思路：
1。将第一待排序序列第一个元素做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2。从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
'''

def insertioSort(arr):
	for i in range(len(arr)):
		preIndex=i-1
		current=arr[i]
		while preIndex>=0 and arr[preIndex]>current:
			arr[preIndex+1]=arr[preIndex]
			preIndex-=1
		arr[preIndex+1]=current
	return arr
arr=[3,2,8,7,5,0,4]
print(insertioSort(arr))

