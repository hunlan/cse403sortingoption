import random

def partition(lst, left, right, pivot):
  pivotValue = lst[pivot]
  tmp = lst[right]
  lst[right] = lst[pivot]
  lst[pivot] = tmp
  storeIndex = left
  for i in range(left, right):
    if lst[i] < pivotValue:
      tmp = lst[i]
      lst[i] = lst[storeIndex]
      lst[storeIndex] = tmp
      storeIndex += 1
  tmp = lst[storeIndex]
  lst[storeIndex] = lst[right]
  lst[right] = tmp
  return storeIndex

def quicksort(lst, left, right):
  if left < right:
    pivot = random.randint(left, right)
    pivotNewIndex = partition(lst, left, right, pivot)
    quicksort(lst, left, pivotNewIndex - 1)
    quicksort(lst, pivotNewIndex + 1, right)

def sort(lst):
  quicksort(lst, 0, len(lst)-1);
  return lst
