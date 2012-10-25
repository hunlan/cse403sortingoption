import radixsort, mergesort, quicksort, bubblesort
import unittest

TEST_URLS = './test_urls.txt'

class RadixTestCase(unittest.TestCase):
  def setUp(self):
    # Set up test list of urls
    # sort the list using a python library and store in this object
    f = open(TEST_URLS, 'r')
    self.unsorted = list(url.strip(' \n') for url in f)
    self.expected = list(self.unsorted)
    self.expected.sort()

  def test_radix(self):
    retlist = radixsort.sort(self.unsorted)
    self.assertEqual(retlist, self.expected)

  def test_merge(self):
    retlist = mergesort.sort(self.unsorted)
    self.assertEqual(retlist, self.expected)

  def test_quicksort(self):
    retlist = quicksort.sort(self.unsorted)
    self.assertEqual(retlist, self.expected)

  def test_bubblesort(self):
    retlist = bubblesort.sort(self.unsorted)
    self.assertEqual(retlist, self.expected)

if __name__ == '__main__':
  unittest.main()
