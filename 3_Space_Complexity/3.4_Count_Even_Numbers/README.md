# Count Even Numbers
**Topic:** Space Complexity

**Type:** Home Challenge


Problem Statement: 

 Given an array of integers, count how many elements are even. 

Input Format: 

An integer n. 

An array of n integers. 

Output Format: 

An integer count of even numbers. 

Constraints: 

1 <= n <= 10^5 

-10^9 <= arr[i] <= 10^9 

Example: 

Input: [2, 5, 6, 7, 8]   
Output: 3   
  

 

### Approach
Describe your approach here...

### Pseudocode
function count_even_numbers(arr):
  // Initialize a counter for even numbers to zero
  count = 0
  
  // Iterate through each element in the input array `arr`
  for each number in arr:
    // Check if the number is evenly divisible by 2
    if number modulo 2 equals 0:
      // If it is, increment the counter
      count = count + 1
  
  // Return the final count
  return count


### Time Complexity
O(n)

### Space Complexity
O(1)
