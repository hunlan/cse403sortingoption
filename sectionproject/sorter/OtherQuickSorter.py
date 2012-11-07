'''
Created on Nov 6, 2012

@author: hunlan
'''
from sectionproject.sorter.Sorter import Sorter
from sectionproject.sorter.othersorters import quicksort

class OtherQuickSorter(Sorter):
    
    @staticmethod
    def sort(urls):
        return quicksort.sort(urls)