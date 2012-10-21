'''
Created on Oct 18, 2012

@author: hunlan
'''
from heapq import heappush, heappop

def GodSort(urls):
    node = Node(urls.pop())
    for url in urls:
        node.insert(url)
        
    return node.getSorted()

def MergeSort(urls):
    if len(urls) <= 1:
        return urls
    
    mid = len(urls) / 2
    left = MergeSort(urls[:mid])
    right = MergeSort(urls[mid:])
    return _merge(left, right)

def HeapSort(urls):
    heap = []
    ret = []
    for value in urls:
        heappush(heap, value)
    
    while(len(heap)>0):
        ret.append(heappop(heap))
    return ret

def InsertSort(urls):
    sorted_urls = [urls.pop()]
    for url in urls:
        for i in range(0, len(sorted_urls)):
            if url < sorted_urls[i]:
                sorted_urls.insert(i, url)
                break
            if i == len(sorted_urls) - 1:
                sorted_urls.append(url)
    return sorted_urls

def _merge(left, right):
    i = 0
    j = 0
    sort = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1
            
    while i < len(left):
        sort.append(left[i])
        i += 1
        
    while j < len(right):
        sort.append(right[j])
        j += 1
            
    return sort

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data
    
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    def getSorted(self):
        ret = []
        if self.left:
            ret.extend(self.left.getSorted())
        ret.append(self.data)
        if self.right:
            ret.extend(self.right.getSorted())
        return ret
