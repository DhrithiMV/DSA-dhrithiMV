# Sort an Array Using Merge Sort
**Topic:** Merge Sort
**Type:** In-Session
Problem :
Implement the Merge Sort algorithm to sort an integer array. 
You are not allowed to use built-in sorting functions. You must implement merge and recursive division logic yourself. 
Example 
Input: 
arr = [5, 2, 3, 1] 
  
Output:  
[1, 2, 3, 5] 
  
Constraints 
1 <= arr.length <= 10^5 
-10^9 <= arr[i] <= 10^9 
 
### Approach
Use the standard divide-and-conquer recursive Merge Sort algorithm. Recursively split the array into halves, sort each, then merge sorted halves with a merge function.

### Pseudocode:
FUNCTION mergeSort(arr):
    IF length(arr) <= 1:
        RETURN arr
    mid = length(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    RETURN merge(left, right)

FUNCTION merge(left, right):
    result = []
    i = 0, j = 0
    WHILE i < length(left) AND j < length(right):
        IF left[i] < right[j]:
            APPEND left[i] to result
            i += 1
        ELSE:
            APPEND right[j] to result
            j += 1
    APPEND remaining elements from left and right to result
    RETURN result

### Time Complexity: O(n log n)

### Space Complexity: O(n)
