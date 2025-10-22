# Two Sum with Multiple Pairs
**Topic:** Hashtables

**Type:** Home Challenge


Problem :

Given an array of integers nums and an integer target, find all distinct pairs of indices (i, j) such that nums[i] + nums[j] == target. Each index can only be used once per pair, and pairs should be unique (no duplicates). Return a list of all pairs sorted by the first index in ascending order. 

This problem expands the original by requiring all valid pairs, handling duplicates efficiently, and ensuring unique pairs without repeats. 

Examples 

Input: nums = [1][2][3][4][3], target = 6 

Output: [[1][3], [2][4]] 

Explanation: 

nums[1] + nums[3] = 2 + 4 = 6 

nums[2] + nums[4] = 3 + 3 = 6 

No other pairs sum to 6. 

Input: nums = [2][7][11][15], target = 9 

Output: [[0][1]] 

Explanation: Only the pair (0,1) sums to 9. 

Input: nums = [3][3][3], target = 6 

Output: [[0][1], [0][2], [1][2]] 

Explanation: All pairs of indices where nums equal 3 sum to 6. 

Input: nums = [1][5][1][5], target = 6 

Output: [[0][1], [0][3], [2][1], [2][3]] 

Explanation: Multiple pairs of 1 and 5 sum to 6, distinct indices for each pair. 

### Approach
Describe your approach here...

### Pseudocode

Initialize an empty dictionary (hashmap)  
For each index i and element num in nums:
 Compute complement = target - num  
 If complement in hashmap, return indices [hashmap[complement], i]  
 Else, store num in hashmap with its index  
Return empty if not found

### Example

Input: nums = [2,7,11,15], target = 9  
Output: [0,1]

### Time Complexity

O(n)

### Space Complexity

O(n)
