'''
Created on Nov 20, 2012

UrlCanonicalizer is a class that normalize a url to the
canonicalized form as described below

@author: hunlan
'''
import re
from sectionproject.urlutils.urlvalidator.urlvalidator import UrlValidator

class UrlCanonicalizer:
    def __init__(self):
        self._reset()
        
    def _reset(self):
        self.canourl = None
    
    '''
    The canonicalize rules are:
    - Preserve Semantics
    1) (host)    lowercase hostname
    2) (path)    decode valid percent encoded 
    3) (port)    remove port
    4) (userpass)remove userpassword
    
    - Result in Equivalent URLs
    5) (path)    add trailing slash
    6) (path)    remove dot-segments
    
    - Change Semantics
    X)   NOT removing path
    7) (fragment)Removing Fragment
    X)   NOT translating from DNS to Domain name (takes too long)
    X)   NOT limiting protocols
    8) (path)    Removing duplicate slashes
    9) (hostname)Removing www
    10) (query)  Sorting query param (lowercase) and use '&' for separating key value pair
    11) (query)  Removing empty query
    '''
    def canonicalizeUrl(self, url):
        uv = UrlValidator()
        if not uv.validate(url):
            raise Exception('invalid url')

        return self.canonicalizerValidator(uv)
        
    def canonicalizerValidator(self, uv):
        if not uv.isUrlValid():
            raise Exception('invalid url')
        
        self.canourl = ''
        
        # append scheme
        scheme = uv.getScheme()
        if scheme != None and scheme != '':
            # add scheme
            self.canourl += scheme 
        
        # 4) No user password
        #
        
        # 1) lowercase url (is done by default from validator)
        hostName = uv.getHostName()
        hostName = hostName.lower()
        
        # 9) remove www. and append hostname
        hostName = self._removeWWWDot(hostName)
        self.canourl += hostName
        
        # 3) No port number
        #
        
        # Path
        #
        # 2) decode path
        path = uv.getDecodedPath()
        if path != None and path != '':
            # 5) Add trailing slash
            path = self._addTrailingSlash(path)
            
            # 8) remove duplicate slashes
            path = self._removeDoubleSlash(path)
            assert(path.endswith('/'))
            
            # 6) remove dot
            path = self._removeDot(path)
            assert(path.endswith('/'))
            assert(not('./' in path))
         
            # append path
            self.canourl += path
        else:
            self.canourl += '/'
        
        # Query
        query = uv.getQuery()
        
        if query != None and query != '':
            # 10) sort query by key
            query = self._sortQueryByKey(query)
            
            # 11) remove empty query
            query = '' if query == '?' else query
            
            # append query
            self.canourl += query
            
        # 7) Remove fragment
        #
        
        return self.canourl
     
    # remove www. from url
    def _removeWWWDot(self, url):
        if not url.startswith('www.'):
            return url[:]
        
        allOccurance = UrlValidator.getAllOccurance(url, '.')
        if len(allOccurance) < 2:
            # case of www.com
            return url[:]
        
        return url[4:]
        
    # remove trailing slash from url
    def _addTrailingSlash(self, url):
        if url.endswith('/'):
            return url[:]
        else:
            return url[:] + '/'
    
    # remove ./ and ../ from url and go back one if it is ../
    def _removeDot(self, url):
        yourl = url[:]
        while './' in yourl:
            idx = yourl.find('./')
            prev_char = yourl[idx-1] if idx > 0 else ''
            if prev_char == '.':
                prev_slash_idx = yourl[:idx].rfind('/')
                prev_prev_slash_idx = yourl[:prev_slash_idx].rfind('/')
                if prev_prev_slash_idx != -1:
                    yourl = yourl[:prev_prev_slash_idx] + yourl[idx+1:]
                else:
                    yourl = yourl[:idx-1] + yourl[idx+2:]
                continue
            
            yourl = yourl[:idx] + yourl[idx + 2:]
        return yourl
    
    # remove double slash
    def _removeDoubleSlash(self, url):
        yourl = url[:]
        while '//' in yourl:
            idx = yourl.find('//')
            yourl = yourl[:idx] + yourl[idx + 1:]
            
        return yourl
            
    # sort query key value
    def _sortQueryByKey(self, q):
        assert q.startswith('?')
        q_noqmark = q.lower()
        q_noqmark = q_noqmark[1:]
        if q_noqmark == '':
            return '?'
        
        kvs = re.split(';|&', q_noqmark)
        kvs.sort()
        
        ret = '?'
        for kv in kvs:
            ret += kv + '&'
        
        return ret[:-1]
        
        
        
        
        
        