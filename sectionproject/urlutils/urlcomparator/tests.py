"""
Testing UrlComparator

There are little comments for each testcase because the name
of each testcase is very descriptive
"""

from django.test import TestCase
from sectionproject.urlutils.urlcomparator.urlcomparator import UrlComparator

class ComparatorTest(TestCase):
    # input: wiki example in writeup
    # expected: equal
    def test_wikiExample(self):
        urlA = 'http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations'
        urlB = 'http://en.wikipedia.org/wiki/Unit_testing#Language-'
        
        expected = 0
        res = UrlComparator.compareNormalizeUrl(urlA, urlB)
        
        self.assertEqual(expected, res, 'expected: ' + str(expected) +\
                                         ', actual: ' + str(res))
      
    # input: two different url
    # expected: one larger than the other, viceversa for opposite direction  
    def test_normalGreaterLesser(self):
        urlA = 'www.google.com'
        urlB = 'www.nba.com'
        
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlA, urlB) < 0)
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlB, urlA) > 0)
        
    # input: one url with www., one without
    # expected: correct behavior
    def test_normalizedWWWDotDifferentUrl(self):
        urlA = 'www.google.com'
        urlB = 'nba.com'
        
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlA, urlB) < 0)
    
    # inputs: url with same query in different order
    # expected equal
    def test_normalizedEqualDifferentQueryUrl(self):
        urlA = 'www.google.com/?q=cse403;id=1'
        urlB = 'www.google.com/?id=1&q=cse403'
        
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlA, urlB) == 0)
    
    # input: url with capital letters in path
    # expected: capital letter should come before 
    def test_caseSensitiveCases(self):
        urlA = 'www.google.com/Images'
        urlB = 'www.google.com/images'
        
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlA, urlB) < 0)
        
    # input: two urls
    # expected: order by alphabetical order
    def test_sourcecomparison(self):
        urlA = 'www.google.com'
        urlB = 'nba.com'
        self.assertTrue(UrlComparator.compareSourceUrl(urlA, urlB) > 0)
    
    # input: a url and two list where one has exactly the same url
    # expected: source unique for one and not source unique for the other
    def test_sourceUnique(self):
        url = 'www.google.com'
        list1 = ['google.com', 'http://google.com']
        list2 = ['www.google.com', 'something.net']
        
        self.assertTrue(UrlComparator.isSourceUnique(url, list1))
        self.assertFalse(UrlComparator.isSourceUnique(url, list2))
        
    # input: a url compared to 1) same url, 2) different but same norm url, 3) entirely
    #        different url
    # expected: 1) False, 2) False, 3) True    
    def test_normunique(self):
        url = 'http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations'
        # same url
        list1 = ['http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations']
        
        # norm same url
        list2 = ['http://en.wikipedia.org/wiki/Unit_testing#Language-']
        
        # different url
        list3 = ['wikipedia.org']
        
        self.assertFalse(UrlComparator.isNormalizeUnique(url, list1))
        self.assertFalse(UrlComparator.isNormalizeUnique(url, list2))
        self.assertTrue(UrlComparator.isNormalizeUnique(url, list3))
        
        
        
    
    
    
    
    
    