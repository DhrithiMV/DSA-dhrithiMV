# Arithmetic Progression Check
**Topic:** Math Essentials

**Type:** Home Challenge

Problem 4: Arithmetic Progression Check 

Difficulty: Easy 
Topics: Array, Sorting 

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same. 

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false. 

Example 1: 

Input: arr = [3,5,1] 
Output: true 
Explanation: We can reorder as [1,3,5] or [5,3,1] with differences 2 and -2 respectively. 
 

Example 2: 

Input: arr = [1,2,4] 
Output: false 
Explanation: There is no way to reorder the elements to obtain an arithmetic progression. 
 

Constraints: 

2 <= arr.length <= 1000 

-10^6 <= arr[i] <= 10^6 

### Approach
Describe your approach here...

### Pseudocode
function canMakeArithmeticProgression(arr):
  // Sort the input array in place.
  sort arr
  
  // Handle the edge case where the array has 2 or fewer elements.
  // In this case, an arithmetic progression is always possible.
  if length of arr <= 2:
    return true
    
  // Calculate the common difference using the first two elements.
  diff = arr[1] - arr[0]
  
  // Iterate through the rest of the array starting from the third element.
  for i from 2 to length of arr - 1:
    // Check if the difference between consecutive elements is equal to the initial common difference.
    if arr[i] - arr[i - 1] is not equal to diff:
      // If any consecutive difference is not the same, it's not an arithmetic progression.
      return false
      
  // If the loop completes without finding any inconsistent differences, it is an arithmetic progression.
  return true


### Time Complexity
O(nlogn)
### Space Complexity
O(n)
