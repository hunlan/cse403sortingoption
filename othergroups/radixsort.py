NUM_BUCKETS = 256

def sort(strings):
  """
  create list of 256 empty lists
  get number of passes by iterating through input list and taking max
  for i = maxlength - 1 to 0
    for each url
      if i >= len(url) 
        put into 0th bucket
      else
        hash each url into bucket based on ith char
      collect buckets into new list
  return collected buckets
  """
  buckets = list([] for i in range(0, NUM_BUCKETS));
  maxlength = max(map(len, strings))
  # count backwards from maxlength - 1 to 0
  for i in range(maxlength - 1, -1, -1):
    for url in strings:
      if (i >= len(url)):
        buckets[0].append(url)
      else:
        char = ord(url[i])
        buckets[char].append(url)
    strings = []
    for bucket in buckets:
      strings.extend(bucket)
    buckets = list([] for i in range(0, NUM_BUCKETS));
  return strings 
