# Reverse an Array
**Topic:** Space Complexity

**Type:** In-Session



Problem Statement: 

 Given an array of integers, reverse the array in-place and return it. 

Input Format: 

An integer n (size of the array). 

An array of n integers. 

Output Format: 

The reversed array. 

Constraints: 

1 <= n <= 10^5 

-10^4 <= arr[i] <= 10^4 

Example: 

Input: [1, 2, 3, 4, 5]   
Output: [5, 4, 3, 2, 1]   
  

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
