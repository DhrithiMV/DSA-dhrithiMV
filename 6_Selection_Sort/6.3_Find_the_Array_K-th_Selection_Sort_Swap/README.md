# Find the Array K-th Selection Sort Swap
**Topic:** Selection Sort
**Type:** Home Challenge
Problem :
Problem: Track Selection Sort Process 
You are given an integer array nums and an integer k. 
 Simulate the Selection Sort process, and return the array after the k-th swap is performed. 
If the algorithm performs fewer than k swaps in total, return the fully sorted array. 
 
Example 1 
Input: nums = [64, 25, 12, 22, 11], k = 2 
Output: [11, 12, 25, 22, 64] 
 
 
Explanation: 
- Swap 1: [11, 25, 12, 22, 64] 
- Swap 2: [11, 12, 25, 22, 64] 
Since k = 2, return after second swap. 
  
Example 2 
Input: nums = [5, 3, 4, 1, 2], k = 10 
Output: [1, 2, 3, 4, 5] 
 
 
Explanation: 
- Selection sort completes in only 4 swaps. 
- Since k > 4, return final sorted array. 
  
Constraints 
1 <= nums.length <= 5000 
-10^5 <= nums[i] <= 10^5 
1 <= k <= 10^6 
 
Follow-up 
Can you optimize the simulation to stop early when no swaps are needed? 
How would this problem change if we asked for the array after k iterations instead of k swaps? 

Approach:
Simulate selection sort. After each swap, increment a counter. When k swaps have occurred, return the array state. If sorting completes before k swaps, return the final sorted array.

Pseudocode:
FUNCTION kthSwapSelectionSort(nums, k):
    swaps = 0
    FOR i FROM 0 TO length(nums) - 1:
        min_idx = i
        FOR j FROM i+1 TO length(nums) - 1:
            IF nums[j] < nums[min_idx]:
                min_idx = j
        IF min_idx != i:
            SWAP nums[i] <-> nums[min_idx]
            swaps += 1
            IF swaps == k:
                RETURN nums
    RETURN nums

Time Complexity:
O(n^2): For each element we look at all subsequent elements

Space Complexity:
O(1): Sorting is done in-place
