# Unique Permutations
**Topic:** Math Essentials

**Type:** Home Challenge

Problem : 

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order. 

Example 1: 

Input: nums = [1,1,2] 
Output: [[1,1,2], [1,2,1], [2,1,1]]M 

Example 2: 

Input: nums = [1,2,3] 
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 

Constraints: 

1 <= nums.length <= 8 

-10 <= nums[i] <= 10 

### Approach
Describe your approach here...

### Pseudocode
function permuteUnique(nums):
  // Initialize a list to store the results.
  res = []
  
  // Sort the input array to handle duplicates efficiently.
  sort(nums)
  
  // Define a recursive backtracking function.
  function backtrack(current_perm, remaining_nums):
    // Base case: If no numbers are remaining, a full permutation is formed.
    if length(remaining_nums) is 0:
      add a copy of current_perm to res
      return
      
    // Iterate through the remaining numbers.
    for i from 0 to length(remaining_nums) - 1:
      // Skip duplicates: If the current number is the same as the previous number and
      // it has not been used in this recursive level, skip it.
      if i > 0 and remaining_nums[i] is equal to remaining_nums[i-1]:
        continue
        
      // Choose:
      // Get the current number to be added.
      num = remaining_nums[i]
      // Create a new list of remaining numbers by removing the chosen one.
      new_remaining = remaining_nums without element at index i
      // Add the chosen number to the current permutation.
      add num to current_perm
      
      // Recurse:
      // Call backtrack with the updated lists.
      backtrack(current_perm, new_remaining)
      
      // Backtrack:
      // Remove the last added number to explore other possibilities.
      remove last element from current_perm
      
  // Start the backtracking process.
  backtrack([], nums)
  
  // Return the list of all unique permutations.
  return res


### Time Complexity
O(n.n!)

### Space Complexity
O(n)
