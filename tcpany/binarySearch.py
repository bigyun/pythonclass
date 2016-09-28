#!/usr/bin/env python

lists=[[0,5],[7,11],[15,19],[20,29],[30,37],[57,68],[69,73],[74,94],]
def BinarySearch(lists, target): 
    low = 0
    high = len(lists) - 1
 
    while low <= high:
        mid = (low + high) // 2
        midVal = lists[mid]
 
        if midVal[1] < target:
            low = mid + 1
        elif midVal[0] > target:
            high = mid - 1
        else:
            return mid
    return -1
print 8//3
