'''
Created on Oct 18, 2012

@author: hunlan
'''
class SortType:
    BINARY_SORT = 'binary'
    MERGE_SORT = 'merge'
    HEAP_SORT = 'heap'
    INSERT_SORT = 'insert'
    
    _ALL = [BINARY_SORT, MERGE_SORT, HEAP_SORT, INSERT_SORT]
    
    @staticmethod
    def isSortType(type):
        if type in SortType._ALL:
            return True
        else:
            return False