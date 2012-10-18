'''
Created on Oct 18, 2012

@author: hunlan
'''
class InputFile(object):
    def __init__(self, str):
        #TODO: Check input and raise Exception()
        mylist = str.split('\n')
        self.sorttype = mylist[0]
        self.urls = self.__parseurl(mylist[1:])
        
    def getSortType(self):
        return self.sorttype
    
    def getUrls(self):
        return self.urls
    
    def __parseurl(self, urls):
        mylist = filter(lambda s: s.strip(), urls)
        return mylist