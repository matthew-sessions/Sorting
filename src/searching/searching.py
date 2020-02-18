# STRETCH: implement Linear Search				
import time

def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if target == arr[i]:
      return i

  return(-1)


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  lenth = len(arr)
  if lenth == 0:
    return -1 # array empty
    
  low = 0
  high = lenth
  while low <= high:
    middle = (high + low) // 2
    if target == arr[middle]:
      return(middle)
    elif target > arr[middle]:
      low = middle + 1
    else:
      high = middle - 1




  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  while low <= high:
    middle = (high + low) // 2
    if target == arr[middle]:
      return(middle)
    elif target > arr[middle]:
      return(binary_search_recursive(arr, target, middle+1, high))
    else:
      return(binary_search_recursive(arr, target, low, middle-1))




a = [i for i in range(500000)]
b = [i for i in range(500000)]

start_time = time.time()
linear_search(a, 4999)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
binary_search(b, 4999)
print("--- %s seconds ---" % (time.time() - start_time))