# Array Sorting with Duplicates
**Topic:** Insertion Sort
**Type:** Home Challenge
Problem : Sort Array By Parity Given an array of integers nums, sort the array using insertion sort such that all even numbers come before all odd numbers. 
Numbers with the same parity can appear in any order (relative order doesn't matter). 
Use insertion sort to maintain stability, inserting each element into the correct parity group by shifting others right. This problem mimics sorting by a custom key (parity), similar to ordering records by category in a PostgreSQL-backed microservice. It introduces handling duplicates and custom comparison logic. Constraints: 
1 ≤ nums.length ≤ 5 × 10^4 
0 ≤ nums[i] ≤ 10^9 Example: 
Input: nums = [3,1,2,4] 
Output: [2,4,3,1] (or any order where evens [2,4] precede odds [3,1]) Why It Fits: Requires adapting insertion sort to a binary condition (even/odd), reinforcing key-based sorting while keeping array operations simple. 
 
### Approach
Use insertion sort with a custom comparison. For each element, compare parity (even = 0, odd = 1) with others in the sorted part. Even values are considered "smaller," so all evens move before odds.
### Pseudocode
```
FUNCTION sortByParity(nums):
    FOR i FROM 1 TO length(nums) - 1:
        key = nums[i]
        j = i - 1
        WHILE j >= 0 AND (nums[j] is odd AND key is even):
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
    RETURN nums
```
### Time Complexity
- O(n²): In the worst case, each new element may move past all others of opposite parity.
### Space Complexity
- O(1): The sort is in-place, so only constant extra space is used.
