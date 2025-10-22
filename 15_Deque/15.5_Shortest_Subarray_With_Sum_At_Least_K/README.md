# Shortest Subarray With Sum At Least K
**Topic:** Deque

**Type:** Home Challenge


Problem :

Given an integer array nums and an integer k, find the length of the shortest non-empty subarray with sum at least k. Return -1 if none. 

Input and Output Explanation 

Input: Array nums and integer k. 

Output: Integer representing length of shortest qualifying subarray, or -1 if none. 

Examples 

Input: nums=[2,-1,2], k=3 
 Output: 3 
 Explanation: Whole array sums to 3. 

Input: nums=[1][2], k=4 
 Output: -1 
 Explanation: No subarray sums to 4. 

Input: nums=[1][2][3][4][5], k=11 
 Output: 3 

Input: nums=[84,-37,32,40,95], k=167 
 Output: 3 

### Approach
Describe your approach here...

### Pseudocode

Initialize two deques — one for min, one for max  
For i in range(k):
 Maintain decreasing order in max_dq  
 Maintain increasing order in min_dq  
Add first window result = min + max  
For each subsequent element:
 Remove indices out of window (i - k)  
 Pop smaller elements for max_dq update  
 Pop larger elements for min_dq update  
 Add current index  
 Add current window’s min + max to total_sum  
Return total_sum

### Example

Input: [2, 5, -1, 7, -3, -1, -2], k = 4  
Output: 18

### Time Complexity

O(n)

### Space Complexity

O(k)
