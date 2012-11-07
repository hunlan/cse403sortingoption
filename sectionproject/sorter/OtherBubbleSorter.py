'''
Created on Nov 6, 2012

@author: hunlan
'''
from sectionproject.sorter.Sorter import Sorter
from sectionproject.sorter.othersorters import bubblesort

class OtherBubbleSorter(Sorter):
    
    @staticmethod
    def sort(urls):
        return bubblesort.sort(urls)