'''
Created on Oct 18, 2012

This class manages the dirty work for parsing an input and 
determining which sorting alg to use

@author: hunlan
'''
from sectionproject.sorter.SortType import SortType
from sectionproject.sorter.InsertionSorter import InsertionSorter
from sectionproject.sorter.HeapSorter import HeapSorter
from sectionproject.sorter.MergeSorter import MergeSorter
from sectionproject.sorter.BinarySorter import BinarySorter
from sectionproject.sorter.OtherMergeSorter import OtherMergeSorter
from sectionproject.sorter.OtherBubbleSorter import OtherBubbleSorter
from sectionproject.sorter.OtherQuickSorter import OtherQuickSorter
from sectionproject.sorter.OtherRadixSorter import OtherRadixSorter

class InputFile(object):
    def __init__(self, type, str):
        if not (SortType.isSortType(type)) :
            print('input type is ' + type + ', not in SortType')
            raise Exception()

        self.sorttype = type
        mylist = str.split('\n')
        self.urls = self.__parseurl(mylist)
        
    def getSortType(self):
        return self.sorttype
    
    def getUrls(self):
        return self.urls
    
    def sortUrls(self):
        if self.sorttype == SortType.BINARY_SORT :
            return BinarySorter.sort(self.urls);
        
        if self.sorttype == SortType.MERGE_SORT:
            return MergeSorter.sort(self.urls)
        
        if self.sorttype == SortType.HEAP_SORT:
            return HeapSorter.sort(self.urls)
        
        if self.sorttype == SortType.INSERT_SORT:
            return InsertionSorter.sort(self.urls)
        
        # Other groups
        if self.sorttype == SortType.OTHER_BUBBLE_SORT:
            return OtherBubbleSorter.sort(self.urls)
        
        if self.sorttype == SortType.OTHER_MERGE_SORT:
            return OtherMergeSorter.sort(self.urls)
        
        if self.sorttype == SortType.OTHER_QUICK_SORT:
            return OtherQuickSorter.sort(self.urls)
        
        if self.sorttype == SortType.OTHER_RADIX_SORT:
            return OtherRadixSorter.sort(self.urls)
        
        raise Exception('unexpected error, no sorting alg found')
    
    def __parseurl(self, urls):
        mylist = filter(lambda s: s.strip(), urls)
        return mylist