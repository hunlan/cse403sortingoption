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
from sectionproject.urlutils.urlvalidator.urlvalidator import UrlValidator
from sectionproject.urlutils.urlcanonicalizer.urlcanonicalizer import UrlCanonicalizer

class InputFile(object):
    def __init__(self, type, validate, str):
        if not (SortType.isSortType(type)) :
            print('input type is ' + type + ', not in SortType')
            raise Exception()

        self.sorttype = type
        self.validate = validate
        mylist = str.split('\n')
        self.urls = self.__parseurl(mylist)
        
    def getSortType(self):
        return self.sorttype
    
    def isValidate(self):
        return self.validate
    
    def getUrls(self):
        return self.urls
    
    def __getNormalizedUrl(self):
        yourl = self.urls[:]
        ret = []
        for url in yourl:
            uv = UrlValidator()
            if uv.validate(url):
                uc = UrlCanonicalizer()
                ret.append(uc.canonicalizerValidator(uv))
            else:
                ret.append(None)
            
        return ret
    
    def sortUrls(self):
        yourls = self.urls[:]
        
        if self.validate:
            validate_urls = self.__getNormalizedUrl()
            assert(len(self.urls) == len(validate_urls))
            
            val_url = []
            inval_url = []
            for i in range(0, len(validate_urls)):
                cur_url = validate_urls[i]
                if cur_url == None:
                    inval_url.append('invalid: ' + self.urls[i])
                else:
                    val_url.append(cur_url)
                    
            sorted_urls = self._sortUrls(val_url)
            
            result = []
            result.extend(inval_url)
            result.extend(['----------sorted urls----------'])
            result.extend(sorted_urls)

            return result
        else:
            return self._sortUrls(yourls)
    
    def _sortUrls(self, urls):
        
        if self.sorttype == SortType.BINARY_SORT :
            return BinarySorter.sort(urls);
        
        if self.sorttype == SortType.MERGE_SORT:
            return MergeSorter.sort(urls)
        
        if self.sorttype == SortType.HEAP_SORT:
            return HeapSorter.sort(urls)
        
        if self.sorttype == SortType.INSERT_SORT:
            return InsertionSorter.sort(urls)
        
        # Other groups
        if self.sorttype == SortType.OTHER_BUBBLE_SORT:
            return OtherBubbleSorter.sort(urls)
        
        if self.sorttype == SortType.OTHER_MERGE_SORT:
            return OtherMergeSorter.sort(urls)
        
        if self.sorttype == SortType.OTHER_QUICK_SORT:
            return OtherQuickSorter.sort(urls)
        
        if self.sorttype == SortType.OTHER_RADIX_SORT:
            return OtherRadixSorter.sort(urls)
        
        raise Exception('unexpected error, no sorting alg found')
    
    def __parseurl(self, urls):
        mylist = filter(lambda s: s.strip(), urls)
        return mylist