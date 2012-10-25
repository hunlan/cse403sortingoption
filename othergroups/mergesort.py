def sort (strings):
  if len(strings) <= 1:
    return strings

  left = sort(strings[:len(strings)/2])
  right = sort(strings[len(strings)/2:])
  
  return merge (left, right)	

def merge (left, right):
  result = []
  leftIndex = 0
  rightIndex = 0

  while leftIndex < len(left) or rightIndex < len(right):
    if leftIndex < len(left) and rightIndex < len(right):
      if left[leftIndex] <= right[rightIndex]:
        result = result + [left[leftIndex]]
        leftIndex = leftIndex + 1
      else: 
        result = result + [right[rightIndex]]
        rightIndex = rightIndex + 1
    elif rightIndex >= len(right):
      result = result + left[leftIndex:]
      leftIndex = leftIndex + len(left[leftIndex:])
    elif leftIndex >= len(left):
      result = result + right[rightIndex:]
      rightIndex = rightIndex + len(right[rightIndex:])

  return result

