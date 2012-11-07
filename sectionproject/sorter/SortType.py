'''
Created on Oct 18, 2012

@author: hunlan
'''
class SortType:
    BINARY_SORT = 'binary'
    MERGE_SORT = 'merge'
    HEAP_SORT = 'heap'
    INSERT_SORT = 'insert'
   
    OTHER_BUBBLE_SORT = 'other_bubble'
    OTHER_MERGE_SORT = 'other_merge'
    OTHER_QUICK_SORT = 'other_quick'
    OTHER_RADIX_SORT = 'other_radix'
    
    
    _ALL = [BINARY_SORT, MERGE_SORT, HEAP_SORT, INSERT_SORT, \
            
            OTHER_MERGE_SORT, OTHER_BUBBLE_SORT, \
            OTHER_QUICK_SORT, OTHER_RADIX_SORT]
    
    @staticmethod
    def isSortType(type):
        if type in SortType._ALL:
            return True
        else:
            return False