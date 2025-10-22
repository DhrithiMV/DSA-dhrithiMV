# Delivering Boxes from Storage to Ports
**Topic:** Queue

**Type:** Home Challenge

Problem :

You need to deliver boxes from storage to ports using a ship. The ship has limits on both the maximum number of boxes it can carry (maxBoxes) and the total weight it can carry (maxWeight). Boxes must be delivered in the order they appear. Each box is represented as [port, weight]. 

You want to minimize the total number of ship trips made. Each trip consists of: 

Loading consecutive boxes respecting maxBoxes and maxWeight. 

Delivering boxes in the order loaded. Switching ports counts as new trip segments. 

A return trip from last port to storage. 

Examples: 

Input: 

boxes = [[1,2],[1,2],[2,1],[2,1]] 
 portsCount = 2 
 maxBoxes = 3 
 maxWeight = 3 
  
 

Output: Minimum number of trips = 4 
 Explanation: Delivered boxes in two shipments to minimize trips while respecting constraints. 

Input: 

boxes = [[1,2],[2,4],[1,1],[2,1],[3,2]] 
 portsCount = 3 
 maxBoxes = 3 
 maxWeight = 6 
  
Output: 6 


Input: 

boxes = [[1,1]] 
 portsCount = 1 
 maxBoxes = 1 
 maxWeight = 1 
  

Output: 2 

Input: 

boxes = [[1,2],[1,2],[1,2]] 
 portsCount = 1 
 maxBoxes = 3 
 maxWeight = 6 

Output: 3 

Constraints: 

Number of boxes up to 10^5. 

1 <= portsCount, maxBoxes, maxWeight <= 10^5. 

Boxes must be delivered in order. 

### Approach
Describe your approach here...

### Problem

Deliver boxes from storage to various ports while respecting ship constraints:
- maxBoxes: maximum number of boxes per trip
- maxWeight: maximum total weight per trip
Find the minimum number of trips required.

### Pseudocode

Precompute weight prefix sum ws and port-change prefix sum cs  
Initialize deque dq with [0] and dp array  
For i = 1 to n:
 Remove indices from dq violating box or weight constraints  
 dp[i] = cs[i-1] - cs[dq[0]] + dp[dq[0]] + 2  
 Maintain deque monotonicity by removing worse previous states  
Return dp[n]

### Time Complexity

O(n)

### Space Complexity

O(n)
