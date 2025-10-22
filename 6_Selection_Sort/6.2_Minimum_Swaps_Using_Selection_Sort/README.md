# Minimum Swaps Using Selection Sort
**Topic:** Selection Sort
**Type:** Home Challenge
Problem :
Problem: Count the Number of Swaps 
You are given an integer array nums. 
 Sort the array in non-decreasing order using Selection Sort, and return the number of swaps performed during the process. 
⚠️ Important: A swap happens only if the minimum element is different from the current position. 
 
Example 1 
Input: nums = [64, 25, 12, 22, 11] 
 
Output: 3 
Explanation: 
- First swap: [11, 25, 12, 22, 64] 
 
- Second swap: [11, 12, 25, 22, 64] 
 
- Third swap: [11, 12, 22, 25, 64] 
 
Total swaps = 3 
  
Example 2 
Input: nums = [1, 2, 3, 4] 
 
Output: 0 
Explanation: 
Already sorted, so no swaps are needed. 
  
 
Constraints 
1 <= nums.length <= 2000 
-10^5 <= nums[i] <= 10^5 
Follow-up 
Can you prove that Selection Sort always performs at most n-1 swaps? 
Why might Selection Sort be preferred in situations where swaps are expensive, even though it's O(n^2)? 
### Approach
Use selection sort but count a swap only if the minimum element is not already at index i. Each time you swap, increment the swap counter.

### Pseudocode
```
FUNCTION minimumSwaps(nums):
    swaps = 0
    FOR i FROM 0 TO length(nums) - 1:
        min_idx = i
        FOR j FROM i+1 TO length(nums) - 1:
            IF nums[j] < nums[min_idx]:
                min_idx = j
        IF min_idx != i:
            SWAP nums[i] <-> nums[min_idx]
            swaps = swaps + 1
    RETURN swaps
```

### Time Complexity
O(n^2): For each element we look at all subsequent elements

### Space Complexity
O(1): Sorting is done in-place
