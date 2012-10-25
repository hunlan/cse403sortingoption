"""

Assume all characters are in ASCII.
input: a file containing a list of URLs. Each URL starts in a new line.
output: a list of sorted strings

"""

import sys, random
import quicksort, bubblesort, mergesort, radixsort

def do_radixsort(strings):
  return radixsort.sort(strings) 

def do_mergesort(strings):
  return mergesort.sort(strings)

def do_quicksort(strings):
  return quicksort.sort(strings)

def do_bubblesort(strings):
  return bubblesort.sort(strings)

def get_strings(f):
  strings = []
  line = f.readline()
  while len(line) > 0:
    # do not add empty line
    if len(line) > 1:
      strings.append(line[:len(line) - 1])
    line = f.readline()
  return strings

if __name__ == "__main__":
  filename = None
  if len(sys.argv) < 3:
    print 'Usage: python main.py input-file output-file'
  else:
    inputfile = open(sys.argv[1])
    strings = get_strings(inputfile)

    # sorting
    print 'Which sorting algorithm would you like?'
    print '1) O(n^2)  2) O(nlogn)  3) O(1)'
    sorting_method = raw_input('Enter: ')
    option = -1
    try:
      option = int(sorting_method[:1])
    except ValueError:
      sys.exit(1)
 
    results = strings
    if option == 1:
      results = do_bubblesort(strings)
    elif option == 3:
      results = do_radixsort(strings)
    elif option == 2:
      num = random.randint(0, 9)
      if num % 2 == 0: 
        results = do_mergesort(strings)
      else: 
        results = do_quicksort(strings)

    outputfile = open(sys.argv[2], 'w+')
    for item in results:
      outputfile.write('%s\n' % item)

    inputfile.close()
    outputfile.close()
