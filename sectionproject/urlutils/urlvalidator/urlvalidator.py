'''
Created on Nov 20, 2012

UrlValidator is a class that validates whether a url is a 
valid url and stores various information about that url.

@author: hunlan
'''
import re

class UrlValidator():
    # Support these 3 scheme only
    SCHEME = ['http', 'https', 'ftp']
    
    # Support these domain
    DOMAIN_LIST = ['.aero', '.asia', '.biz', '.cat', \
                   '.com', '.coop', '.edu', '.gov', \
                   '.info', '.int', '.jobs', '.mil', \
                   '.mobi', '.museum', '.name', '.net', \
                   '.org', '.pro', '.tel', '.travel', '.xxx']
    
    # speical characters in url
    STOP_SYM_AFTER_PATH = ['/', '?', '#', ':', '@']
    
    # valid url char inaddition to 0-9 a-z A-Z
    VALID_URI_CHAR = ['-', '_']
    
    # exception character in fragment
    FRAGMENT_EXCEPTION = ['&', ';', '=']
    
    '''
    Initialize class variables
    '''
    def __init__(self):
        self._reset()
    
    '''
    @Override
    toString method
    mainly for debugging
    '''
    def __str__(self):
        string = ''
        string += 'full url: ' + self.yourl + '\n'
        
        string += 'scheme:   '
        string += self.scheme if self.scheme != None else 'None'
        string += '\n'
        
        string += 'userpass: '
        string += self.userPassword if self.userPassword != None else 'None'
        string += '\n'
        
        string += 'hostType: ' + HostEnum.getString(self.hostType) + '\n' +\
                    'hostName: ' + self.hostName + '\n'
    
        string += 'port:     '
        string += self.port if self.port != None else 'None'
        string += '\n'
        
        string += 'path:     '
        string += self.path if self.path != None else 'None'
        string += '\n'
        
        string += 'query:    '
        string += self.query if self.query != None else 'None'
        string += '\n'
        
        string += 'fragment: '
        string += self.fragment if self.fragment != None else 'None'
        
        return  string
    
    '''
    reset class variable
    '''
    def _reset(self):
        self.yourl = None
        self.scheme = None
        self.userPassword = None
        self.hostType = None
        self.hostName = None
        self.port = None
        self.path = None
        self.query = None
        self.fragment = None
        self.isValid = False
    
    '''
    This method takes in a url and return whether the url is valid or not
    This method also stores some data about the url
    @param url Input URL to validate
    @return True if validate url, false otherwise
    '''
    def validate(self, url):
        assert isinstance(url, str)
        self._reset()
        
        # copy url
        yourl = url[:]
        self.yourl = url[:]
        
        # Remove scheme if there is one
        prev = yourl[:]
        yourl = self._isSchemeNameValid(yourl)
        if yourl == '':
            self.scheme = prev
        else:
            if yourl == prev:
                self.scheme = None
            else:
                self.scheme = prev[:prev.find(yourl)]        
        
        # check if there is user/password and remove it
        prev = yourl[:]
        yourl = self._isUserPasswordValid(yourl)
        if yourl == None:
            return False
        if yourl == '':
            self.userPassword = prev
        else:
            if yourl == prev:
                self.userPassword = None
            else:
                self.userPassword = prev[:prev.find(yourl)]
        
        # check the type of host name (IPv4 or Domain Name) 
        host = self._whichHostType(yourl)
        self.hostType = host
        
        # perform check on IPv4 or Domain Name
        prev = yourl[:]
        if host == HostEnum.NOHOST:
            return False
        elif host == HostEnum.DOMAIN:
            yourl = self._isDomainNameValid(yourl)
            if yourl == None:
                return False
        elif host == HostEnum.IPv4:
            yourl = self._checkAndRemoveIPv4(yourl)
            if yourl == None:
                return False
        
        if yourl == '':
            self.hostName = prev
        else:
            if yourl == prev:
                self.hostName = None
            else:
                self.hostName = prev[:prev.find(yourl)] 
                
        # perform check on Port if there is one
        prev = yourl[:]
        yourl = self._isPortNumberValid(yourl)
        if yourl == None:
            return False
        if yourl == '':
            self.port = prev
        else:
            if yourl == prev:
                self.port = None
            else:
                self.port = prev[:prev.find(yourl)]
        
        
        # perform check on path
        prev = yourl[:]
        yourl = self._isPathValid(yourl)
        if yourl == None:
            return False
        if yourl == '':
            self.path = prev
        else:
            if yourl == prev:
                self.path = None
            else:
                self.path = prev[:prev.find(yourl)]
        
        # check query
        prev = yourl[:]
        yourl = self._isQueryValid(yourl)
        if yourl == None:
            return False
        if yourl == '':
            self.query = prev
        else:
            if yourl == prev:
                self.query = None
            else:
                self.query = prev[:prev.find(yourl)]
        
        # check Fragment
        prev = yourl[:]
        yourl = self._isFragmentValid(yourl)
        if yourl == None:
            return False
        
        if yourl == '':
            self.fragment = prev
        else:
            if yourl == prev:
                self.fragment = None
            else:
                self.fragment = prev[:prev.find(yourl)]
        
        
        # print yourl # for debugging
        self.isValid = '' == yourl
        return self.isValid
    
    
    
    
    '''
    This method check if scheme name is valid
    @param url A URL input
    @return Returns url with no scheme if valid,
            Returns copy of url if do not have scheme
    '''
    def _isSchemeNameValid(self, url):
        yourl = url.lower()
        # remove optional scheme if exist
        for sh in self.SCHEME:
            if yourl.startswith(sh):
                idx = url.find('://')
                if idx != -1 and idx == len(sh):
                    return url[idx+3:]
        return url[:]
    
    '''
    This method check if user/password is valid
    An Authority with user/password must have a '@' character and 
    a colon ':', and the colon must come before the '@' character 
    @param url A URL input with scheme removed
    @return Returns None if scheme is not valid, 
            Returns url with no user/password if valid
    '''
    def _isUserPasswordValid(self, url):
        # search for "@", if doesn't appear, url doesn't have user/password
        at_idx = url.find("@")
        if at_idx == -1:
            return url[:]
        
        # check if colon exist, and if it exist, if there is only one
        #  colon between begining and @
        colon_idx_list = self.getAllOccurance(url, ':')
        if len(colon_idx_list) == 0:
            # Fail if no colon
            return None
        elif len(colon_idx_list) == 1:
            if colon_idx_list[0] > at_idx:
                # Fail if no colon between beginnign and @
                return None 
        else:
            if not(colon_idx_list[0] < at_idx and colon_idx_list[1] > at_idx):
                # Fail if there is 2 colons pior to @ symbol
                return None 
        
        colon_idx = colon_idx_list[0]
        # some string processing to get out username and password
        stop_idx = self.__getFirstOccurance(url[colon_idx+1:], self.STOP_SYM_AFTER_PATH)               
        username = url[:colon_idx]
        password = url[colon_idx+1:]
        if stop_idx != -1:
            password = url[colon_idx+1:colon_idx+1+stop_idx]
                        
        if  username != '' and \
            password != '' and \
            self.__checkValidUrlChar(username) and \
            self.__checkValidUrlChar(password):
            # valid username and password            
            return url[at_idx+1:]
        else:
            # invalid username or password
            return None

    '''
    Validate which host type (IPv4 or Domain Name)
    TODO: NOTE: CURRENTLY DO NOT SUPPORT IPv6
    TODO: NOTE: DO NOT SUPPORT 'localhost'
    Determine host type by
    1) the number of "." 
    2) then see if between the . are letters or numbers

    Domain Name e.g.
    1 period: google.com          | OK
    2 period: www.google.com      | OK
    3 period: www.google.com.hk   | Not OK   (kinna confuse about this one thou)
    
    IPv4 Example
    3 period: 127.0.0.1           | OK
    
    
    Note, this method does not check if the host type is valid or not
    it only give suggestion what that type is base on number of dot
    '''
    def _whichHostType(self, url):
        dot_count = 0
        stop_idx = self.__getFirstOccurance(url[:], self.STOP_SYM_AFTER_PATH)               
        hostname = url[:]
        if stop_idx != -1:
            hostname = hostname[:stop_idx]
            
        remain = hostname[:]
        idx = remain.find(".")
        while idx != -1:
            dot_count += 1
            remain = remain[idx + 1:]
            idx = remain.find(".")
            
        if dot_count == 0:
            # no period = fail
            return HostEnum.NOHOST
        if dot_count < 3:
            # valid domain name
            return HostEnum.DOMAIN
        elif dot_count == 3:
            # three period, potentially a ipv4
            return HostEnum.IPv4
        else:
            # too many period
            return HostEnum.NOHOST
    
    '''
    Detects whether the Domain name is valid or not
    @param url A URL input with everything before domain name  removed
    @return Returns None if scheme is not valid, 
            Returns url with no Domain if valid
    '''
    def _isDomainNameValid(self, url):
        yourl = url.lower()
        # for all the domain ending list (e.g. .com, .org, etc)
        for rhs in self.DOMAIN_LIST:
            if rhs in yourl:
                # end with a valid domain end
                idx = yourl.find(rhs)
                domain = url[:idx]
                d_list = domain.split('.')
                if len(d_list) > 2:
                    # www.something.abc.com is invalid
                    return None
                else:
                    # check if valid url characters
                    for s in d_list:
                        if s == '' or not self.__checkValidUrlChar(s):
                            return None
                # return success
                return url[idx+len(rhs):]
        # not valid ending
        return None
    
    '''
    Detects whether IPv4 is valid or not
    @param url A URL input with everything before IPv4 removed
    @return Returns None if scheme is not valid, 
            Returns url with no IPv4 if valid
    '''
    def _checkAndRemoveIPv4(self, url):
        remain = url[:]
        for i in range(0, 3):
            # find "."
            idx = remain.find('.')
            if idx == -1:
                return None
            number = self.__getNextInteger(remain[:idx],3)
            if number == None:
                # not a number
                return None
            
            if number < 0 or number > 255:
                # not a number between 0 and 255
                return None
            # cut number
            remain = remain[idx+1:]
        
        # if no more remain
        if len(remain) == 0:
            return None
        
        # if still have period
        if '.' in remain:
            return None
        
        
        # check last integer
        number = self.__getNextInteger(remain[:], 3)
        if number == None:
            return None
        
        if number < 0 or number > 255:
            return None
        
        return remain[idx:]
    
    '''
    Check and remove Port number
    @param url A URL input with everything before Port removed
    @return Returns None if scheme is not valid, 
            Returns url with no Port if valid
    '''
    def _isPortNumberValid(self, url):
        if url.startswith(':') :
            next_int = self.__getNextInteger(url[1:], 16)
            if next_int == None:
                return None
            if next_int < 0 or next_int > 65535:
                return None
            idx = len(':') + len(str(next_int))
            return url[idx:]
        else :
            return url[:]
    
    '''
    Check and remove Path
    @param url A URL input with everything before Path removed
    @return Returns None if scheme is not valid, 
            Returns url with no Path if valid
    '''
    def _isPathValid(self, url):
        if url.startswith('/') :
            # if have a slash then its a path
            copy_url = url[:]
            # process whenever there is slash
            while copy_url.startswith('/'):
                # remove slash
                copy_url = copy_url[1:]
                
                # get occurance of stopwords
                idx = self.__getFirstOccurance(copy_url, \
                                                   self.STOP_SYM_AFTER_PATH)               
                
                if idx == -1:
                    # no valid stop words ==> everything after = path
                    if not self.__validatePath(copy_url):
                        #not valid path because everything after is not valid characters
                        return None
                    
                    # check percent symbols
                    replaced = UrlValidator.replacePercentSymbols(copy_url)
                    if replaced == None:
                        # not valid percent symbols
                        return None
                    
                    # removed everything
                    return ''
                
                a_path = copy_url[:idx]
                replaced = UrlValidator.replacePercentSymbols(a_path)
                if replaced == None:
                    return None
                
                if not self.__validatePath(a_path):
                    return None
                
                copy_url = copy_url[idx:]
                
            return copy_url
        else :
            # no path, still valid
            return url[:]
    
    '''
    Check and remove Query
    TODO NOTE: numeric value can be key values 
    @param url A URL input with everything before Query removed
    @return Returns None if Query is not valid, 
            Returns url with no Query if valid
    '''
    def _isQueryValid(self, url):
        if url.startswith('?') :
            frag_idx = url.find('#')
            ret = '' if frag_idx == -1 else url[frag_idx:]
            parse = url[1:] if frag_idx == -1 else url[1:frag_idx]
            
            if parse == '':
                # short circuit on empty query
                return ret
            
            field_value_list = re.split(';|&', parse)
            for fv in field_value_list:
                if not self.__validateFieldValuePair(fv):
                    return None
            return ret
        else:
            return url[:]
    
    # fragment can be a-z, A-Z, 0-9, -, _, =, &, ;
    '''
    Check and remove Fragment
    @param url A URL input with everything before Fragment removed
    @return Returns None if Fragment is not valid, 
            Returns url with no Fragment if valid
    '''
    def _isFragmentValid(self, url):
        if url.startswith('#'):
            url_after = url[1:]
            isvalid = self.__checkValidUrlChar(url_after, self.FRAGMENT_EXCEPTION)
            if isvalid:
                return ''
            else:
                return None
        else:
            return url[:]
    
    ########################################################################
    #----------------------Private Class Methods---------------------------#
    ########################################################################
    
    # since field and value can be anything, only thing to check
    # is that '=' is in fv adn that '=' is not at index 0
    def __validateFieldValuePair(self, fv):
        if not '=' in fv:
            return False
        
        equal_idx = fv.find('=')
        if equal_idx == 0:
            return False
        
        key = fv[:equal_idx]
        value = fv[equal_idx + 1:]
        nextInt = self.__getNextInteger(key, 3)
        if nextInt != None:
            return False
        return self.__checkValidUrlChar(key) and \
                self.__checkValidUrlChar(value)
    
    # check if path uses valid characters (note, ./ and ../ is also valid)
    def __validatePath(self, path):
        paths = path.split('/')
        for p in paths:
            # check if it is ..
            if p == '.' or p == '..':
                continue
            
            if not self.__checkValidUrlChar(p, ['%']) :
                return False 
        return True
    
    # replace percent symbol with ascii version, return None if not
    # replaceable
    @staticmethod
    def replacePercentSymbols(url_path):
        path = url_path[:]
        while '%' in path:
            idx = path.find('%')
            if idx + 3 > len(path) :
                # dont have 2 character after %
                return None
            symbol = path[idx+1:idx+3]
            hex_int = None
            try:
                hex_int = int(symbol, 16)
            except Exception:
                return None
            
            try:
                converted = chr(hex_int)
                one = path[:idx]
                two = path[idx+3:]
                path = one + converted + two
            except Exception:
                return None          
        return path
    
    # Given a string, get next integer
    def __getNextInteger(self, url, max):        
        # check last integer
        remain = url[:]
        hasZeroAhead = False
        while remain.startswith('0'):
            hasZeroAhead = True
            remain = remain[1:]
        c = ''
        idx = 0
        for i in range(0,max):
            try:
                if remain[i] != '.':
                    c += remain[i]
                    int(c)
                    idx += 1
                else :
                    if i == 0 and hasZeroAhead:
                        return 0
                    elif i == 0:
                        return None
                    return int(c[:idx])
            except Exception:
                if i == 0 and hasZeroAhead:
                    return 0
                elif i == 0:
                    return None
                return int(c[:idx])
        return int(c[:])
    
    # check if string uses valid url characters
    def __checkValidUrlChar(self, string, ex_list = None):
        if len(string) == 0:
            return True
        list_words = self.VALID_URI_CHAR[:]
        if ex_list != None:
            list_words.extend(ex_list)
            
        new_string = string[:]
        for st in list_words:
            new_string = new_string.replace(st,'')
        return new_string == '' or new_string.isalnum()

    # Helper method to get first occurance of any char in list_char in 
    # string
    def __getFirstOccurance(self, string, list_char):
        idx = -1
        for stopword in list_char:
            new_idx = string.find(stopword)
            if idx == -1:
                idx = new_idx
            elif new_idx != -1:
                idx = min(idx, new_idx)
        return idx
    
    # Get all occurance of char in string
    @staticmethod
    def getAllOccurance(string, char):
        lis = []
        newstring = string[:]
        while char in newstring:
            idx = newstring.find(char)
            lis.append(idx)
            newstring = newstring[idx+1:]
        return lis
    
    #####################################################
    ## GETTERS
    #####################################################    
    def getYourl(self):
        return self.yourl
    
    def getScheme(self):
        return self.scheme
    
    def getUserPassword(self):
        return self.userPassword        
    
    def getHostType(self):
        return self.hostType

    def getHostName(self):
        return self.hostName
    
    def getPort(self):
        return self.port
    
    def getPath(self):
        return self.path
    
    def getDecodedPath(self):
        if self.path == None:
            return None
        return UrlValidator.replacePercentSymbols(self.path)
    
    def getQuery(self):
        return self.query
    
    def getFragment(self):
        return self.fragment
    
    def isUrlValid(self):
        return self.isValid

'''
Enum class that describes hostname type
'''
class HostEnum():
    NOHOST = -1
    DOMAIN = 0
    IPv4 = 1
    
    @staticmethod
    def getString(type):
        if type == 0:
            return 'Domain'
        elif type == 1:
            return 'IPv4'
        else:
            return 'No Host'