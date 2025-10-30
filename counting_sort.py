"""
How it works:
*************

1. Create a new array for counting how many there are of the different values.
2. Go through the array that needs to be sorted.
3. For each value, count it by increasing the counting array at the corresponding index.
4. After counting the values, go through the counting array to create the sorted array.
5. For each count in the counting array, create the correct number of elements, with values that 
   correspond to the counting array index.
   
Conditions for Counting Sort
****************************
These are the reasons why Counting Sort is said to only work for a limited range of non-negative integer values:

1. Integer values: Counting Sort relies on counting occurrences of distinct values, so they must be integers. 
   With integers, each value fits with an index (for non negative values), and there is a limited number of 
   different values, so that the number of possible different values k is not too big compared to the number of 
   values n.
2. Non negative values: Counting Sort is usually implemented by creating an array for counting. When the algorithm 
   goes through the values to be sorted, value x is counted by increasing the counting array value at index x. 
   If we tried sorting negative values, we would get in trouble with sorting value -3, because index -3 would be 
   outside the counting array.
3. Limited range of values: If the number of possible different values to be sorted k is larger than the number 
   of values to be sorted n, the counting array we need for sorting will be larger than the original array we have 
   that needs sorting, and the algorithm becomes ineffective., the counting array we need for sorting will be 
   larger than the original array we have that needs sorting, and the algorithm becomes ineffective.
"""

def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)
