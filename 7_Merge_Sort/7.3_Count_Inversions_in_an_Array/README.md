# Count Inversions in an Array
**Topic:** Merge Sort
**Type:** Home Challenge
Problem :
An inversion in an array is a pair of indices (i, j) such that: 
i < j and 
arr[i] > arr[j]. 
You need to count the total number of inversions in the given array. 
 Solve this problem using Merge Sort in O(n log n) time. 
 Example 1 
Input: 
arr = [2, 4, 1, 3, 5] 
  
Output:  
3 
  
Explanation:  Inversions are (2,1), (4,1), (4,3) → total 3. 
 
Example 2 
Input: 
arr = [5, 4, 3, 2, 1] 
  
Output: 10 
  
Explanation: Every pair is inverted. 
 
Constraints 
1 <= arr.length <= 10^5 
-10^9 <= arr[i] <= 10^9 
 
### Approach
Use modified Merge Sort to count inversions. Whenever an element from the right half is placed before an element from the left half during merge, accumulate inversions by counting remaining elements in left half. This achieves O(n log n) inversion counting.

### Pseudocode
```
FUNCTION countInversions(arr):
    IF length(arr) <= 1:
        RETURN arr, 0
    mid = length(arr) // 2
    left, inv_left = countInversions(arr[:mid])
    right, inv_right = countInversions(arr[mid:])
    merged, inv_merge = merge_and_count(left, right)
    RETURN merged, inv_left + inv_right + inv_merge

FUNCTION merge_and_count(left, right):
    result = []
    i = j = inv_count = 0
    WHILE i < length(left) AND j < length(right):
        IF left[i] <= right[j]:
            result.APPEND(left[i])
            i += 1
        ELSE:
            result.APPEND(right[j])
            inv_count += length(left) - i
            j += 1
    APPEND remaining elements
    RETURN result, inv_count
```

### Time Complexity
O(n log n)

### Space Complexity
O(n)
