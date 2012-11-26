"""
Testing UrlCanonicalizer

There are no comments for each testcase because the name
of each testcase is very descriptive
"""

from django.test import TestCase
from sectionproject.urlutils.urlcanonicalizer.urlcanonicalizer import UrlCanonicalizer
from sectionproject.urlutils.urlvalidator.urlvalidator import UrlValidator

class UrlCanonicalizerTest(TestCase):
    def test_wikiexample(self):
        urls = ['http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations',\
                'http://en.wikipedia.org/wiki/Unit_testing#Language-']
        expected = ['http://en.wikipedia.org/wiki/Unit_testing/',\
                    'http://en.wikipedia.org/wiki/Unit_testing/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)
            
    def test_lowercaseHostName(self):
        urls = ['www.GoOgLE.com',\
                'http://en.wIkipediA.org/wiki/Unit_testing#Language-']
        expected = ['google.com/',\
                    'http://en.wikipedia.org/wiki/Unit_testing/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)
            
    def test_decodePercentEncoding(self):
        urls = ['www.GoOgLE.com/hunlan%40gmail%2ecom',\
                'cs.washington.edu/%43%53%45%34%30%33',\
                'http://en.wIkipediA.org/wiki/Unit_testing/%4f%4F#Language-']
        expected = ['google.com/hunlan@gmail.com/',\
                    'cs.washington.edu/CSE403/',\
                    'http://en.wikipedia.org/wiki/Unit_testing/OO/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)    
    
    def test_removePort(self):
        urls = ['www.GoOgLE.com:80/hunlan%40gmail%2ecom',\
                'http://en.wIkipediA.org:0/wiki/Unit_testing/%4f%4F#Language-']
        expected = ['google.com/hunlan@gmail.com/',\
                    'http://en.wikipedia.org/wiki/Unit_testing/OO/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)        
            
    
    def test_removeUserPassword(self):
        urls = ['hunlan:password@www.GoOgLE.com:80/hunlan%40gmail%2ecom',\
                'http://wiki:pedia@en.wIkipediA.org:0/wiki/Unit_testing/%4f%4F#Language-']
        expected = ['google.com/hunlan@gmail.com/',\
                    'http://en.wikipedia.org/wiki/Unit_testing/OO/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)        
            
    def test_addtrailingslash(self):
        urls = ['http://google.com/path',\
                'http://wiki:pedia@en.wIkipediA.org:0/wiki/Unit_testing/%4f%4F#Language-']
        expected = ['http://google.com/path/',\
                    'http://en.wikipedia.org/wiki/Unit_testing/OO/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)       
            
    def test_removeDotSegments(self):
        urls = ['http://google.com/path/../path',\
                'http://google.com/.././path',\
                'http://wiki:pedia@en.wIkipediA.org:0/wiki/Unit_testing/%2e%2e#Language-']
        expected = ['http://google.com/path/',\
                    'http://google.com/path/',\
                    'http://en.wikipedia.org/wiki/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)       
            
            
    def test_removeFragment(self):
        urls = ['http://google.com/path/../path#fragment',\
                'http://wiki:pedia@en.wIkipediA.org:0/wiki/Unit_testing/%2e%2e#Language-']
        expected = ['http://google.com/path/',\
                    'http://en.wikipedia.org/wiki/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)       
                    
    def test_removeDupSlashes(self):
        urls = ['http://google.com//path//..///path////////////',\
                'http://wiki:pedia@en.wIkipediA.org:0//wiki/Unit_testing/%2e%2e#Language-']
        expected = ['http://google.com/path/',\
                    'http://en.wikipedia.org/wiki/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)       
            
                        
    def test_removeWWWdot(self):
        urls = ['http://www.google.com//path//..///path////////////']
                
        expected = ['http://google.com/path/']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual)  
            
    def test_sortAndUseAndSignForQuery(self):
        urls = ['www.nba.com?a=0;A=1;a=d',\
                'http://google.com//path//..///path////////////?b=2;a=1',\
                'http://wiki:pedia@en.wIkipediA.org:0//wiki/Unit_testing/%2e%2e?a=0;c=1&B=2#Language-']
        expected = ['nba.com/?a=0&a=1&a=d',\
                    'http://google.com/path/?a=1&b=2',\
                    'http://en.wikipedia.org/wiki/?a=0&b=2&c=1']
        
        for i in range(0,len(urls)):
            uc = UrlCanonicalizer()
            actual = uc.canonicalizeUrl(urls[i])
            self.assertEqual(expected[i], actual, \
                             'fail on url: ' + urls[i] + '\n' +\
                             'expected: ' + expected[i] + '\n' +\
                             'actual  : ' + actual) 
             
            
            
            
            
            
            