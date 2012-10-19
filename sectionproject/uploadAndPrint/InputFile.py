'''
Created on Oct 18, 2012

This class manages the dirty work for parsing an input and 
determining which sorting alg to use

@author: hunlan
'''
from sectionproject.uploadAndPrint.SortType import SortType
from sectionproject.uploadAndPrint.Sorter import GodSort, MergeSort, HeapSort,\
    InsertSort

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
        if self.sorttype == SortType.GOD_SORT :
            return GodSort(self.urls);
        
        if self.sorttype == SortType.MERGE_SORT:
            return MergeSort(self.urls)
        
        if self.sorttype == SortType.HEAP_SORT:
            return HeapSort(self.urls)
        
        if self.sorttype == SortType.INSERT_SORT:
            return InsertSort(self.urls)
    
    def __parseurl(self, urls):
        mylist = filter(lambda s: s.strip(), urls)
        return mylist