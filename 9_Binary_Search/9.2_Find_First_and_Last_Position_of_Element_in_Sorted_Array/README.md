# Find First and Last Position of Element in Sorted Array
**Topic:** Binary Search
**Type:** In-Session
Problem : Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found, return [-1, -1]. 
Input Explanation: 
nums: List of integers sorted in ascending order. 
target: Integer value whose start and end positions are to be found. 
Output Explanation: 
List of two integers: [first_index, last_index] indicating the start and end positions of target; [-1, -1] if not present. 
Examples: 
Input: nums = [5,7,7,8,8,10], target = 8 
Output: [3,4] 
Explanation: 8 appears from index 3 to 4. 
 
Input: nums = [1,1,2,2,2,3,4], target = 2 
Output: [2,4] 
Explanation: 2 is found from index 2 to 4. 
 
Input: nums = [1,3,3,3,4,5], target = 6 
Output: [-1,-1] 
Explanation: 6 is not present in the array. 
### Approach
Use binary search twice: once to find the first position of the target, and once for the last position. For each, update answer and narrow search left or right depending on comparison.

### Pseudocode
```
FUNCTION searchRange(nums, target):
    first = findBound(nums, target, True)
    last = findBound(nums, target, False)
    RETURN [first, last]

FUNCTION findBound(nums, target, isFirst):
    left, right = 0, length(nums) - 1
    bound = -1
    WHILE left <= right:
        mid = (left + right) // 2
        IF nums[mid] == target:
            bound = mid
            IF isFirst:
                right = mid - 1
            ELSE:
                left = mid + 1
        ELSE IF nums[mid] < target:
            left = mid + 1
        ELSE:
            right = mid - 1
    RETURN bound
```

### Time Complexity
O(log n)

### Space Complexity
O(1)
