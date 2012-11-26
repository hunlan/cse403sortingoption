'''
Created on Nov 26, 2012

UrlComparator is a class that defines ==, < and >
of urls.

@author: hunlan
'''
from sectionproject.urlutils.urlvalidator.urlvalidator import UrlValidator
from sectionproject.urlutils.urlcanonicalizer.urlcanonicalizer import UrlCanonicalizer

class UrlComparator():
    
    # Determines whether a url is source unique amount url_list
    @staticmethod
    def isSourceUnique(url, url_list):
        for yourl in url_list:
            if UrlComparator.compareSourceUrl(url, yourl) == 0:
                return False
        return True
    
    # Determines whether a url is canonical unique amount url_list
    @staticmethod
    def isNormalizeUnique(url, url_list, raiseException = True):
        for yourl in url_list:
            if UrlComparator.compareNormalizeUrl(url, yourl, raiseException) == 0:
                return False
        return True
    
    '''
    This method compares the raw value of the url
    returns 0  if urlA == urlB
            1  if urlA >  urlB
            -1 if urlA <  urlB
    '''
    @staticmethod
    def compareSourceUrl(urlA, urlB):
        if urlA > urlB:
            return 1
        elif urlA < urlB:
            return -1
        else:
            return 0
    
    '''
    This method compares the normalized value of the urls
    returns 0  if urlA == urlB
            1  if urlA >  urlB
            -1 if urlA <  urlB
    '''
    @staticmethod
    def compareNormalizeUrl(urlA, urlB, raiseException=True):
        uvA = UrlValidator()
        uvB = UrlValidator()
        
        if not uvA.validate(urlA):
            if raiseException:
                raise Exception('Invalid urlA')
            else:
                return -1
        
        if not uvB.validate(urlB):
            if raiseException:
                raise Exception('Invalid urlB')
            else:
                return 1
        
        ucA = UrlCanonicalizer()
        ucB = UrlCanonicalizer()
        
        yourlA = ucA.canonicalizerValidator(uvA)
        yourlB = ucB.canonicalizerValidator(uvB)
        
        if yourlA < yourlB:
            return -1
        elif yourlA > yourlB:
            return 1
        else:
            return 0
        
        