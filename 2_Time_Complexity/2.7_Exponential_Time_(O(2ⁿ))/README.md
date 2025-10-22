# Exponential Time (O(2ⁿ))
**Topic:** Time & Space Complexity
**Type:** Home Challenge
Exponential Time (O(2ⁿ)) 
Statement: Print all subsets of an array. 
Constraints: 1 ≤ n ≤ 20 
Time Complexity: O(2ⁿ) 
Space Complexity: O(2ⁿ) 
Test Cases: 
Input: [1,2] → Output: [], [1], [2], [1,2] 
Input: [3] → Output: [], [3] 
Input: [1,2,3] → Output: 8 subsets 
### Approach
Use backtracking to generate all subsets. Recursively add or skip each element into the current subset.
### Pseudocode
```
FUNCTION generateSubsets(arr, index, subset):
    IF index == length(arr):
        PRINT subset
        RETURN
    generateSubsets(arr, index+1, subset)
    generateSubsets(arr, index+1, subset + [arr[index]])
```
### Time Complexity
O(2ⁿ)
### Space Complexity
O(2ⁿ)
