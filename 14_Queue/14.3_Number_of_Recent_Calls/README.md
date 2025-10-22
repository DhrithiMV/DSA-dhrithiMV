# Number of Recent Calls
**Topic:** Queue

**Type:** Home Challenge

Problem :

Implement a class RecentCounter that counts the number of recent requests within a sliding window of 3000 milliseconds. Each call to ping(t) adds a new request at time t (in milliseconds) and returns how many requests have happened between [t-3000, t] inclusive. 

Examples: 

Input: 

 ping(1)   # returns 1 
 ping(100) # returns 2 
 ping(3001) # returns 3 
 ping(3002) # returns 3 
  
 

Explanation: The requests at times 1, 100, 3001, 3002. 
 For ping at 3002, requests within [^3002] are 3.[1] 

Input: 

 ping(5000)  # returns 1 
 ping(8000)  # returns 1 
 ping(11000) # returns 1 
  
 

Explanation: Each new ping is more than 3000 ms apart, so count resets. 


Input: 

 ping(3000) 
 ping(3002) 
 ping(6000) 
 ping(6001) 
  
 

Returns: 

 1
 2 
 2 
 2 
  
 

Explanation: Sliding window moves, counts accordingly. 

Input: 

 ping(10) 
 ping(3010) 
 ping(6010) 
 ping(9000) 
  
 

Returns: 

 1
 2 
 2 
 2 
  
 

Constraints: 

Calls to ping are made in increasing order of t. 

Up to 10^4 calls. 

1 <= t <= 10^9 

  

### Approach
Describe your approach here...

### Pseudocode

Initialize deque dq and result list  
For i from 0 to n-1:  
    If dq[0] < i - k + 1, remove dq[0]  
    While dq is not empty and nums[dq[-1]] < nums[i], pop dq[-1]  
    Append i to dq  
    If i >= k-1, append nums[dq[0]] to result  
Return result

### Time Complexity

O(n)

### Space Complexity

O(k)

