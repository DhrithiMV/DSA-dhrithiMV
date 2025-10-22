# Remove Duplicates from Sorted Array
**Topic:** Space Complexity

**Type:** Home Challenge

Problem Statement: 

 Given a sorted array, remove duplicates in-place and return the new length. 

Input Format: 

An integer n. 

A sorted array of n integers. 

Output Format: 

The length after removing duplicates. 

Constraints: 

1 <= n <= 10^5 

-10^4 <= arr[i] <= 10^4 

Example: 

Input:  [1, 1, 2, 2, 3]   
Output: 3   
  

### Approach
Describe your approach here...

### Pseudocode
function removeDuplicates(nums):
  // Handle the edge case of an empty input array.
  if nums is empty:
    return 0

  // `write_idx` is the "write" pointer, indicating the position
  // for the next unique element. The first element is always unique.
  write_idx = 1

  // Iterate with a "read" pointer `i` from the second element.
  for i from 1 to length(nums) - 1:
    // Compare the element at `i` with the previous element.
    if nums[i] is not equal to nums[i - 1]:
      // If the elements are different, it's a new unique element.
      // Overwrite the position at `write_idx` with this new element.
      nums[write_idx] = nums[i]
      // Increment the `write_idx` to point to the next available spot.
      write_idx = write_idx + 1

  // The final value of `write_idx` is the count of unique elements.
  return write_idx


### Time Complexity
O(n)

### Space Complexity
O(1)
