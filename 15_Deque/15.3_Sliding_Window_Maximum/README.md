# Sliding Window Maximum
**Topic:** Deque

**Type:** In-Session

Problem :

Given an integer array and a window size k, return an array of the maximum values in every contiguous subarray of size k. 

Input and Output Explanation 

Input: An integer list nums and integer k, the window size. 

Output: A list of integers where each element is the maximum of the corresponding window. 

Examples 

Input: nums=[1,3,-1,-3,5,3,6,7], k=3 
 Output: [3][3][5][5][6][7] 
 Explanation: Windows and max values are: [1,3,-1]=3, [3,-1,-3]=3, [ -1,-3,5]=5, etc. 

Input: nums=[9][5][3][1][2][8], k=2 
 Output: [9][5][3][2][8] 

Input: nums=[2][1], k=2 
 Output: [2] 

### Approach
Describe your approach here...

### Pseudocode

Initialize deque dq and result array res  
For each index i in nums:  
    If dq[0] is out of current window, pop from front  
    While nums[dq[-1]] < nums[i], pop from dq to maintain decreasing order  
    Append i to dq  
    If i >= k-1, append nums[dq[0]] to result  
Return result

### Time Complexity

O(n)

### Space Complexity

O(k)

