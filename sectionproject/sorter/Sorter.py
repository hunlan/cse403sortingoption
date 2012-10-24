'''
Created on Oct 23, 2012

This is an interface for the sorters.

This class must implement sort.

@author: hunlan
'''
class Sorter( object ):
    
    '''
    sort a list of url.
    '''
    @staticmethod
    def sort(list_urls):
        raise NotImplementedError( "Should have implemented this" )