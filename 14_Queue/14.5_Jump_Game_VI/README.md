# Jump Game VI
**Topic:** Queue

**Type:** Home Challenge

Problem :

You are given an integer array nums and an integer k. You start at index 0 and want to reach the last index (n-1). At each step, you can jump to any index i + j where 1 <= j <= k and i + j < n. Your score is the sum of the values of the indices you have visited. Return the maximum score you can get. 

Examples: 

Input: nums = [1, -1, -2, 4, -7, 3], k = 2 
 Output: 7 
 Explanation: One optimal path is 0 -> 3 -> 5. 
 Sum: 1 + 4 + 3 = 8 (Check carefully) 
 Actually max score is 7 here due to jumps. 

Input: nums = [10,-5,-2,4,0,3], k = 3 
 Output: 17 
 Explanation: Path 0 -> 3 -> 5 gives sum 10 + 4 + 3 = 17. 

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2 
 Output: 0 
 Explanation: One path maximizing score is 0 -> 3 -> 5 -> 7. 

Input: nums = [100,-1,-100,-1,100], k = 2 
 Output: 198 
 Explanation: The path 0 -> 2 -> 4 is best with 100 - 100 + 100. 

Constraints: 

1 <= nums.length <= 10^5 

-10^4 <= nums[i] <= 10^4 

1 <= k <= 10^5 

### Approach
Describe your approach here...

### Pseudocode

Initialize max_dq, min_dq as empty deques  
left = 0  
For right from 0 to n-1:  
 While max_dq not empty and nums[right] > max_dq[-1], pop max_dq  
 Append nums[right] to max_dq  
 While min_dq not empty and nums[right] < min_dq[-1], pop min_dq  
 Append nums[right] to min_dq  
 While max_dq[0] - min_dq[0] > limit:  
  If nums[left] == max_dq[0], pop max_dq  
  If nums[left] == min_dq[0], pop min_dq  
  Increment left  
 Update res = max(res, right-left+1)  
Return res

### Time Complexity

O(n)

### Space Complexity

O(n)

