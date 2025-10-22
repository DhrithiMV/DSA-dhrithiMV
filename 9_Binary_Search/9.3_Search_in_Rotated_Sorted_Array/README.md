# Search in Rotated Sorted Array
**Topic:** Binary Search
**Type:** Home Challenge
Problem : Suppose a sorted array is rotated at an unknown pivot index. Given the rotated array nums and an integer target, return the index of target if found; otherwise, return -1. You must write an algorithm with O(log n) runtime complexity. 
Input Explanation: 
nums: List of integers, originally sorted in ascending order, rotated at some unknown pivot. 
target: Integer value to search for. 
Output Explanation: 
Integer index of target in nums if present; otherwise, -1. 
Examples: 
 
Input: nums = [4,5,6,7,0,1,2], target = 0 
Output: 4 
Explanation: 0 is found at index 4 after rotation. 
 
Input: nums = [6,7,8,1,2,3,4,5], target = 8 
Output: 2 
Explanation: 8 is at index 2. 
 
Input: nums = [7,8,1,2,3,4,5,6], target = 5 
Output: 6 
Explanation: 5 is at index 6. 
 
### Approach
Use modified binary search. In each iteration, determine if the left or right half is sorted. Decide which half the target could be in and restrict the search range accordingly.

### Pseudocode
FUNCTION search(nums, target):
    left = 0, right = length(nums) - 1
    WHILE left <= right:
        mid = (left + right) // 2
        IF nums[mid] == target:
            RETURN mid
        IF nums[left] <= nums[mid]:
            IF nums[left] <= target < nums[mid]:
                right = mid - 1
            ELSE:
                left = mid + 1
        ELSE:
            IF nums[mid] < target <= nums[right]:
                left = mid + 1
            ELSE:
                right = mid - 1
    RETURN -1

### Time Complexity
O(log n)

### Space Complexity
O(1)
