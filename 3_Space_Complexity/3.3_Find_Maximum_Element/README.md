# Find Maximum Element
**Topic:** Space Complexity

**Type:** In-Session


Problem Statement: 

 Given an array of integers, find and return the maximum element. 

Input Format: 

An integer n. 

An array of n integers. 

Output Format: 

A single integer (maximum element). 

Constraints: 

1 <= n <= 10^5 

-10^9 <= arr[i] <= 10^9 

Example: 

Input: [3, 7, 2, 9, 5]   
Output: 9   
  

 

 

 

### Approach
Describe your approach here...

### Pseudocode
function reverse_array_inplace(arr):
  // Initialize a left pointer at the beginning of the array.
  left = 0
  // Initialize a right pointer at the end of the array.
  right = length(arr) - 1

  // Loop as long as the left pointer is before the right pointer.
  while left < right:
    // Swap the elements at the left and right pointers.
    swap arr[left] and arr[right]
    
    // Move the left pointer one step to the right.
    left = left + 1
    // Move the right pointer one step to the left.
    right = right - 1
  
  // Return the modified array.
  return arr


### Time Complexity
O(n)

### Space Complexity
O(1)
