# Longest Continuous Subarray With Absolute Diff ≤ K
**Topic:** Queue

**Type:** Home Challenge

Problem :

Given an integer array nums and an integer limit, find the length of the longest continuous subarray such that the absolute difference between any two elements in this subarray is less than or equal to limit. 

Examples: 

Input: nums = [8][2][4][7], limit = 4 
 Output: 2 
 Explanation: The subarray [2][4] has max difference 2, which is ≤ 4. Extending to [2][4][7] yields difference 5 > 4. 

Input: nums = [10][1][2][4][7][2], limit = 5 
 Output: 4 
 Explanation: Subarray [2][4][7][2] is valid; max diff = 5. 

Input: nums = [4][2][2][2][4][4][2][2], limit = 0 
Output: 3 
Explanation: Subarrays with all identical elements like [2][2][2] match the zero difference. 

Input: nums = [1][5][6][7][8][10][6][5][6], limit = 4 
 Output: 5 
 Explanation: The longest valid subarray is [5][6][7][8][10] with max difference 5, but limit is 4, so [6][7][8][10] is not valid. So the subarray is [1][5][6]. Careful check needed.[2][3][4] 

Constraints: 

1 <= nums.length <= 10^5 

1 <= nums[i] <= 10^9 

0 <= limit <= 10^9 

### Approach
Describe your approach here...

### Pseudocode

Initialize empty queue  
On ping(t):  
    Append t to queue  
    Remove leftmost elements < t - 3000  
    Return queue size

### Time Complexity

O(1) amortized per ping

### Space Complexity

O(w), where w is the max number of calls in 3000 ms window

