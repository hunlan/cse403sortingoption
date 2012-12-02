"""
Testing UrlValidator

There are no comments for each testcase because the name
of each testcase is very descriptive
"""

from django.test import TestCase
from sectionproject.urlutils.urlvalidator.urlvalidator import UrlValidator

class UrlValidatorTest(TestCase):
    # setup urlvalidator
    def setUp(self):
        self.urlValidator = UrlValidator()
    
    # wiki example validation, expect true
    def test_wikiexample(self):
        urls = ['http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations',\
                'http://en.wikipedia.org/wiki/Unit_testing#Language-']
        
        for url in urls:
            self.assertTrue(self.urlValidator.validate(url))
    
    # check param input
    def test_illegalinput(self):
        with self.assertRaises(AssertionError) as err:
            self.urlValidator.validate(None)
            
        with self.assertRaises(AssertionError) as err:
            self.urlValidator.validate(123)
            
    # check empty string
    def test_emptystring(self):
        self.assertFalse(self.urlValidator.validate(''))
    
    # scheme
    def test_correct_incorrect_scheme(self):
        correct_list = ['http://www.google.com', \
                        'ftp://www.google.com', \
                        'www.google.com']    
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)
            
        incorrect_list = ['htp://www.google.com', \
                        '://www.google.com', \
                        'http:/www.google.com', \
                        'http//www.google.com']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url), 'fail at url = ' + url)
            
    # uname pword      
    def test_correct_incorrect_usernamepassword(self):
        correct_list = ['http://hunlan:password@www.google.com', \
                        'http://www.google.com']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)
            
        incorrect_list = ['http://hunlan@www.google.com', \
                          'http://hunlan:pass:word@www.google.com', \
                          'http://@www.google.com', \
                          'http://@@www.google.com']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url), 'fail at url = ' + url)
    
    # dname
    def test_correct_incorrect_domainname(self):
        correct_list = ['http://google.com', \
                        'http://cs.washington.edu/path', \
                        'http://555.com']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)
            
        incorrect_list = ['http://.com', \
                          'http://localhost:80', \
                          'http://cs.wash.ing.ton.edu', \
                          'http://www.n*a.com', \
                          'http://www.google.cam',\
                          'http://',\
                          '']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url), 'fail at url = ' + url)
            
    # ipv4
    def test_correct_incorrect_ipv4(self):
        correct_list = ['http://127.0.0.1', \
                        'http://127.0.0.1:8000/path']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)
            
        incorrect_list = ['http://127', \
                          'http://...', \
                          'http://256.0.0.1', \
                          'http://a.a.a.a',\
                          'http://1.2.3',\
                          'http://1.2.3.4.5']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url), 'fail at url = ' + url)
            
    # port
    def test_correct_incorrect_port(self):
        correct_list = ['http://127.0.0.1:8000/url', \
                        'http://www.google.com:80/', \
                        'http://www.google.com/']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)  
            
        incorrect_list = ['http://127.0.0.1:65536', \
                          'http://www.google.com:port0', \
                          'http://www.google.com:']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url)) 
            
    # path
    def test_correct_incorrect_path(self):
        correct_list = ['http://127.0.0.1:8000/url//nba/videos///', \
                        'http://127.0.0.1:8000/%2b', \
                        'http://www.google.com:80/', \
                        'http://www.google.com']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)  
            
        incorrect_list = ['http://www.google.com:80/something@nba.com', \
                          'http://www.google.com/images%', \
                          'http://www.google.com/%2x/']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url)) 
            
    # query
    def test_correct_incorrect_query(self):
        correct_list = ['http://127.0.0.1:8000/url//nba/videos///?nba=cool', \
                        'http://127.0.0.1:8000/%2b?key=val1&key2=val2;key3=3#frag', \
                        'http://www.google.com:80/path/', \
                        'http://www.google.com:80/path/?', \
                        'http://www.google.com:80/path?']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)  
            
        incorrect_list = ['http://www.google.com?nba', \
                          'http://www.google.com/??', \
                          'http://www.google.com/?cmm = cmm', \
                          'http://www.google.com/?key==value', \
                          'http://www.google.com/?1a=1b']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url)) 
            
    # fragment
    def test_correct_incorrect_fragment(self):
        correct_list = ['http://127.0.0.1:8000/url//nba/videos///?nba=cool#fragment', \
                        'http://127.0.0.1:8000/%2b?key=val1&key2=val2;key3=3#_-_', \
                        'http://127.0.0.1:8000/%2b?key=val1&key2=val2;key3=3#', \
                        'http://www.google.com:80/path/']
        for url in correct_list:
            self.assertTrue(self.urlValidator.validate(url), 'fail at url = ' + url)  
            
        incorrect_list = ['http://www.google.com?nba#wrong fragment', \
                          'http://www.google.com/##']
        for url in incorrect_list:
            self.assertFalse(self.urlValidator.validate(url)) 

'''
Test scheme part of url
'''
class SchemeTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
    # input: correct url
    # expected: non-None
    def test_basicCorrectSituation(self):
        valid_scheme_url = ['http://www.google.com', \
                            'https://www.google.com', \
                            'ftp://www.google.com']
        expected = ['www.google.com', \
                    'www.google.com', \
                    'www.google.com']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isSchemeNameValid(valid_scheme_url[i])
            self.assertEqual(expected[i], ret)
    
    # input: incorrect url
    # expected: original url
    def test_wrongSchemeType(self):
        invalid_scheme_url = ['htp://www.google.com', \
                              'www://www.google.com', \
                              'ftp:/www.google.com', \
                              'http//www.google.com']
        for url in invalid_scheme_url:
            ret = self.urlValidator._isSchemeNameValid(url)
            self.assertEqual(url, ret)
        
   # input: no scheme url
    # expected: original url  
    def test_inputWithoutSchemeType(self):
        no_scheme_url = ['', 'www.google.com']
        for url in no_scheme_url:
            ret = self.urlValidator._isSchemeNameValid(url)
            self.assertEqual(url, ret)

'''
Test username password part of url
'''
class UserPasswordTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
    # input: correct username/password
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = ['hunlan:password@gmail.com']
        expected = ['gmail.com']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isUserPasswordValid(urls[i])
            self.assertEqual(expected[i], ret)
            
    # input: incorrect username/password
    # expected: None
    def test_illegalUsernamePassword(self):
        urls = ['hunlan@gmail.com',\
                ':password@gmail.com',\
                'hunlan:pass:word@gmail.com',\
                'hunlan:****@gmail.com',\
                '@gmail.com']
        for url in urls:
            ret = self.urlValidator._isUserPasswordValid(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)
    
    # input: no username and password
    # expected: non-None
    def test_noUsernamePassword(self):
        urls = ['www.gmail.com']
        expected = ['www.gmail.com']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isUserPasswordValid(urls[i])
            self.assertEqual(expected[i], ret)      
        
'''
Test domainname part of url
'''
class DomainNameTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
    # input: correct input
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = ['www.google.com/images',\
                'google.com',\
                'wiki.org/info',\
                'cs.washington.edu/cse403']
        expected = ['/images',\
                    '',\
                    '/info',\
                    '/cse403']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isDomainNameValid(urls[i])
            self.assertEqual(expected[i], ret)
            
    # input: incorrect input
    # expected: None
    def test_illegalDomainName(self):
        urls = ['google/images',\
                'www.google.google.com',\
                'www.g**gle.com',\
                'cs.washington.ed/cse403',\
                '']
        for url in urls:
            ret = self.urlValidator._isDomainNameValid(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)
            
'''
Test IPv4 part of url
'''
class IPv4Test(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
        
    # input: correct input
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = ['127.0.0.1:8000/urls',\
                '127.0.0.1']
        expected = [':8000/urls',\
                    '']
        for i in range(0, len(expected)):
            ret = self.urlValidator._checkAndRemoveIPv4(urls[i])
            self.assertEqual(expected[i], ret)
            
    # input: incorrect input
    # expected: None
    def test_illegalIPv4(self):
        urls = ['127.0.1.',\
                '127.0.1', \
                '0.0.0.256',\
                '0.0.0.-1',\
                'a.b.c.d',\
                '127.0.0.0.1',\
                '123',\
                '']
        for url in urls:
            ret = self.urlValidator._checkAndRemoveIPv4(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)

'''
Test Port part of url
'''
class PortTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
        
    # input: correct input
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = [':8000/urls',\
                ':65535',\
                ':0000000000000000000000000000000000000000000000065535',\
                '']
        expected = ['/urls',\
                    '']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isPortNumberValid(urls[i])
            self.assertEqual(expected[i], ret)
            
    # input: incorrect input
    # expected: None
    def test_illegalPort(self):
        urls = ['::',\
                ':abc', \
                ':-1',\
                ':',\
                ':65536',\
                ':065536']
        for url in urls:
            ret = self.urlValidator._isPortNumberValid(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)
            
    # input: no port
    # expected: original url 
    def test_noPort(self):
        urls = ['/url/paths',\
                '']
        for url in urls:
            ret = self.urlValidator._isPortNumberValid(url)
            self.assertEqual(url, ret, 'wrong val at url: ' + url)
            
            
'''
Test Path part of url
'''
class PathTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
        
    # input: correct input
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = ['/urls?q=a',\
                '//urls//nba/com',\
                '/change%2bmy%2bmood',\
                '/change_my-mood',\
                '/../',\
                '/./',\
                '']
        expected = ['?q=a',\
                    '',\
                    '',\
                    '',\
                    '',\
                    '']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isPathValid(urls[i])
            self.assertEqual(expected[i], ret)
            
    # input: incorrect input
    # expected: None
    def test_illegalPath(self):
        urls = ['/change*my*mood',\
                '/change%xxmymood', \
                '/change%', \
                '/change./', \
                '/ha ha did this slip the test?']
        for url in urls:
            ret = self.urlValidator._isPathValid(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)
            
    # input: no path
    # expected: original url 
    def test_noPath(self):
        urls = ['?q=a',\
                '']
        for url in urls:
            ret = self.urlValidator._isPathValid(url)
            self.assertEqual(url, ret, 'wrong val at url: ' + url)          
            
'''
Test Query part of url
'''
class QueryTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
        
    # input: correct input
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = ['?q=a#fragment',\
                '?a=1&b=2;c=3',\
                '?',\
                '?#fragment']
        expected = ['#fragment',\
                    '',\
                    '',\
                    '#fragment']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isQueryValid(urls[i])
            self.assertEqual(expected[i], ret, 'wrong val at url: ' + urls[i])
            
    # input: incorrect input
    # expected: None
    def test_illegalPath(self):
        urls = ['?a', \
                '?1=2', \
                '?a=*', \
                '?a=1,b=2']
        for url in urls:
            ret = self.urlValidator._isQueryValid(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)
            
    # input: no Query
    # expected: original url 
    def test_noQuery(self):
        urls = ['#fragment',\
                '']
        for url in urls:
            ret = self.urlValidator._isQueryValid(url)
            self.assertEqual(url, ret, 'wrong val at url: ' + url)     
            
            
'''
Test Query part of url
'''
class FragmentTest(TestCase):
    def setUp(self):
        self.urlValidator = UrlValidator()
        
        
    # input: correct input
    # expected: non-None
    def test_basicCorrectSituation(self):
        urls = ['#fragment',\
                '#_-_',\
                '#']
        expected = ['',\
                    '',\
                    '']
        for i in range(0, len(expected)):
            ret = self.urlValidator._isFragmentValid(urls[i])
            self.assertEqual(expected[i], ret, 'wrong val at url: ' + urls[i])
            
    # input: incorrect input
    # expected: None
    def test_illegalPath(self):
        urls = ['##',\
                '#omg this is a fragment?', \
                '#www.google.com']
        for url in urls:
            ret = self.urlValidator._isFragmentValid(url)
            self.assertEqual(None, ret, 'wrong val at url: ' + url)
            
    # input: no Fragment
    # expected: original url 
    def test_noFragment(self):
        urls = ['']
        for url in urls:
            ret = self.urlValidator._isFragmentValid(url)
            self.assertEqual(url, ret, 'wrong val at url: ' + url)   
            
            