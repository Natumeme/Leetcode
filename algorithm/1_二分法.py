#!usr/bin/env python
#-*- coding:utf-8 -*-

def binary_search(list,item):
	low = 0 #low和high用于跟踪要在其中查找的列表部分
	high = len(list)-1

	while low <= high:
		mid = (low + high)//2#只要范围没缩小到只包含一个元素，就检查中间的元素
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None
my_list = [1,3,5,7,9]
print(binary_search(my_list,3))
print(binary_search(my_list,-1))#=> None 在python中，None表示空，它意味着没有找到指定元素
