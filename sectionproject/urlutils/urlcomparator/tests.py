"""
Testing UrlComparator

There are no comments for each testcase because the name
of each testcase is very descriptive
"""

from django.test import TestCase
from sectionproject.urlutils.urlcomparator.urlcomparator import UrlComparator

class ComparatorTest(TestCase):
    def test_wikiExample(self):
        urlA = 'http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations'
        urlB = 'http://en.wikipedia.org/wiki/Unit_testing#Language-'
        
        expected = 0
        res = UrlComparator.compareNormalizeUrl(urlA, urlB)
        
        self.assertEqual(expected, res, 'expected: ' + str(expected) +\
                                         ', actual: ' + str(res))
        
    def test_normalGreaterLesser(self):
        urlA = 'www.google.com'
        urlB = 'www.nba.com'
        
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlA, urlB) < 0)
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlB, urlA) > 0)
        
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
        
    def test_caseSensitiveCases(self):
        urlA = 'www.google.com/Images'
        urlB = 'www.google.com/images'
        
        self.assertTrue(UrlComparator.compareNormalizeUrl(urlA, urlB) < 0)
    
    
    
    
    
    
    
    