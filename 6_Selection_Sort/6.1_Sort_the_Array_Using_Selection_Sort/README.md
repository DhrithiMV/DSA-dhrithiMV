# Sort the Array Using Selection Sort
**Topic:** Selection Sort
**Type:** In-Session

Problem :
Problem: Sort the Array Using Selection Sort 
You are given an integer array nums. 
 Your task is to sort the array in non-decreasing order using the Selection Sort algorithm. 
Selection Sort works as follows: 
For each index i from 0 to n-1: 
Find the minimum element in the subarray [i … n-1]. 
Swap it with the element at index i. 
Continue until the array is sorted. 
You must not use any built-in sort functions. 
 
Example 1 
Input: nums = [64, 25, 12, 22, 11] 
 
Output: [11, 12, 22, 25, 64] 
 
Explanation:  
- First pass: [11, 25, 12, 22, 64] 
- Second pass: [11, 12, 25, 22, 64] 
- Third pass: [11, 12, 22, 25, 64] 
- Fourth pass: [11, 12, 22, 25, 64] (no swap needed) 
  
Example 2 
Input: nums = [5, 1, 4, 2, 8] 
 
Output: [1, 2, 4, 5, 8] 
 
Constraints 
1 <= nums.length <= 1000 
-10^4 <= nums[i] <= 10^4 

Follow-up 
What is the time complexity of selection sort in the worst case? 
Is selection sort stable? Why or why not? 
 
### Approach
Use selection sort to find the minimum in the unsorted part from i to n-1 and swap it with position i. This process is repeated until all elements are sorted.

### Pseudocode
```
FUNCTION selectionSort(nums):
    FOR i FROM 0 TO length(nums) - 1:
        min_idx = i
        FOR j FROM i+1 TO length(nums) - 1:
            IF nums[j] < nums[min_idx]:
                min_idx = j
        SWAP nums[i] <-> nums[min_idx]
    RETURN nums
```

### Time Complexity
O(n^2): For each element we look at all subsequent elements

### Space Complexity
O(1): Sorting is done in-place
