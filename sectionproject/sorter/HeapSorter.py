'''
Created on Oct 23, 2012

@author: YoungMing
'''
from sectionproject.sorter.Sorter import Sorter
from heapq import heappush, heappop

class HeapSorter(Sorter):
    @staticmethod
    def sort(urls):
        heap = []
        ret = []
        for value in urls:
            heappush(heap, value)
        
        while(len(heap)>0):
            ret.append(heappop(heap))
        return ret