'''
Created on Oct 23, 2012

@author: Joon
'''
from sectionproject.sorter.Sorter import Sorter

class MergeSorter(Sorter):
    @staticmethod
    def sort(urls):
        if len(urls) <= 1:
            return urls
        
        mid = len(urls) / 2
        left = MergeSorter.sort(urls[:mid])
        right = MergeSorter.sort(urls[mid:])
        return MergeSorter._merge(left, right)
    
    @staticmethod
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