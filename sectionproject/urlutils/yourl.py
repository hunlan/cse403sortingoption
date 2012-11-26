'''
Created on Nov 19, 2012

@author: hunlan
'''
class YouRL():
    SCHEME = ['http', 'https', 'ftp']
    
    def __init__(self, url):
        lower_uri = url.lower()
        
        
        noscheme = True
        for sch in self.SCHEME:
            if lower_uri.startswith(sch):
                noscheme = False
                break
        if noscheme:
            lower_uri = self.SCHEME[0] + '://' + lower_uri
        
        
        self.original = url
        self.schema = self._getSchemeFromUrl(url)
    
    def getSchema(self):
        return self.schema
    
    def _getSchemeFromUrl(self, url):
        idx = url.find(':')
        return url[0:idx]