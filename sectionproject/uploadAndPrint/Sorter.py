'''
Created on Oct 18, 2012

@author: hunlan
'''
from heapq import heappush

def GodSort(urls):
    return urls

def MergeSort(urls):
    if len(urls) <= 1:
        return urls
    
    mid = len(urls) / 2
    left = MergeSort(urls[:mid])
    right = MergeSort(urls[mid:])
    return _merge(left, right)

def HeapSort(urls):
    heap = []
    for value in urls:
        heappush(heap, value)
    return heap

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