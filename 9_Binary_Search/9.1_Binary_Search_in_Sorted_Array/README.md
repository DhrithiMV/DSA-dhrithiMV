# Binary Search in Sorted Array
**Topic:** Binary Search
**Type:** In-Session
Problem : Given a sorted array of integers nums and an integer target, return the index of target in nums. If target is not found, return -1. 
Input Explanation: 
nums: A list of integers sorted in ascending order. 
target: Integer value to search for. 
Output Explanation: 
Integer index of target in nums if present; otherwise, -1. 
Examples: 
Input: nums = [1,2,3,4,5], target = 3 
Output: 2 
Explanation: 3 is found at index 2 in the array. 
Input: nums = [-10,-3,0,4,8,12], target = 4 
Output: 3 
Explanation: 4 is found at index 3. 
 
Input: nums = [2,4,5,7,10], target = 6 
Output: -1 
Explanation: 6 is not present in the array. 
### Approach
Binary Search compares the target to the middle element of the current search range. If equal, return index. If target is less, search left half, else search right half. Repeat until found or range is empty.
### Pseudocode
```
FUNCTION binarySearch(nums, target):
    left = 0, right = length(nums) - 1
    WHILE left <= right:
        mid = (left + right) // 2
        IF nums[mid] == target:
            RETURN mid
        ELSE IF nums[mid] < target:
            left = mid + 1
        ELSE:
            right = mid - 1
    RETURN -1
```
### Time Complexity
O(log n)
### Space Complexity
O(1)
