'''
Created on Nov 6, 2012

@author: hunlan
'''
from sectionproject.sorter.Sorter import Sorter
from sectionproject.sorter.othersorters import radixsort

class OtherRadixSorter(Sorter):
    
    @staticmethod
    def sort(urls):
        return radixsort.sort(urls)