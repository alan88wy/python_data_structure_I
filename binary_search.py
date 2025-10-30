"""
How it works:
*************

1. Check the value in the center of the array.
2. If the target value is lower, search the left half of the array. If the target value is higher, 
   search the right half.
3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or 
   until the search area is empty.
4. If the value is found, return the target value index. If the target value is not found, return -1.
"""

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")