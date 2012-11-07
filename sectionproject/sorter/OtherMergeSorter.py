'''
Created on Nov 6, 2012

@author: hunlan
'''
from sectionproject.sorter.Sorter import Sorter
from sectionproject.sorter.othersorters import mergesort

class OtherMergeSorter(Sorter):
    @staticmethod
    def sort (urls):
        return mergesort.sort(urls)
