# Contains Duplicate II
**Topic:** Hashtables

**Type:** Home Challenge

Problem :


Given an integer array nums and an integer k, determine if there exist two distinct indices i and j such that nums[i] == nums[j] and the absolute difference between i and j is at most k. 

Return True if such a pair exists; otherwise, return False. 

This problem adds a constraint related to the closeness of duplicate elements, requiring careful handling of indices. 

Examples 

Input: nums = [1][2][3][1], k = 3 

Output: True 

Explanation: The duplicates 1 are at indices 0 and 3, with difference exactly 3. 

Input: nums = [1][0][1][1], k = 1 

Output: True 

Explanation: The duplicates 1 appear at indices 2 and 3, difference is 1. 

Input: nums = [1][2][3][1][2][3], k = 2 

Output: False 

Explanation: Though duplicates exist, no pairs have indices closer or equal to 2. 

Input: nums = [], k = 0 

Output: False 

Explanation: Empty array has no duplicates. 

### Approach
Describe your approach here...

### Pseudocode

Initialize an empty dictionary index_map  
For i, num in enumerate(nums):  
 If num exists in index_map and i - index_map[num] <= k:  
  Return True  
 Else, update index_map[num] = i  
Return False

### Example

Input: nums = [1, 2, 3, 1], k = 3  
Output: True  

Because nums[0] == nums[3] and |0 - 3| = 3 <= k

### Time Complexity

O(n)

### Space Complexity

O(n)
