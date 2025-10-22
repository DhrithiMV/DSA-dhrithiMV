# First Negative Number in Every Window of Size K
**Topic:** Deque

**Type:** Home Challenge

Problem :

Given an integer array and window size k, find the first negative number in every contiguous window of size k. If none, output 0. 

Input and Output Explanation 

Input: Integer list nums, integer k window size. 

Output: List of first negative numbers for each window or 0 if none. 

Examples 

Input: nums=[12,-1,-7,8,-15,30,16,28], k=3 
 Output: [-1, -1, -7, -15, -15, 0] 

Input: nums=[1][2][3][4], k=2 
 Output: [0][0][0] 

Input: nums=[-5,2,-3,1,4], k=2 
 Output: [-5,-3,-3,0] 

### Approach
Describe your approach here...

### Pseudocode

1. Compute prefix sum array
2. Initialize deque to hold indices, maintaining increasing prefix sums
3. For each index i:
   - While current prefix - prefix at deque front >= k:
       update min length and pop from front
   - While deque back has prefix >= current prefix, pop from back
   - Append current index to deque
4. Return -1 if no valid subarray is found, else min length

### Example

Input: nums = [2, -1, 2], k = 3  
Output: 3

### Time Complexity

O(n)

### Space Complexity

O(n)
