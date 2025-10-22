# Sum of Array Elements
**Topic:** Space Complexity

**Type:** In-Session


Problem Statement: 

 Given an array of integers, return the sum of all elements. 

Input Format: 

An integer n. 

An array of n integers. 

Output Format: 

The integer sum. 

Constraints: 

1 <= n <= 10^5 

-10^4 <= arr[i] <= 10^4 

Example: 

Input: [1, 2, 3]   
Output: 6   
  

 

 

 


### Approach
Describe your approach here...

### Pseudocode
function sum_array_elements(arr):
  // Initialize a variable to store the total sum
  total = 0
  
  // Iterate through each element in the input array `arr`
  for each element in arr:
    // Add the current element to the total
    total = total + element
  
  // Return the final total
  return total


### Time Complexity
O(n)

### Space Complexity
O(1)
