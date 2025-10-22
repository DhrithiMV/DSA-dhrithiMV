# Two Sum - Sorted Input
**Topic:** Lists with Two Pointer Techniques

**Type:** In-Session

Problem :

 Given a sorted list nums and a target value target, return the indices (1-based) of two numbers such that they add up to target. Assume exactly one solution exists. Do not use the same element twice. 

Input Explanation: 

nums: Sorted list of integers. 

target: Target sum value. 

Output Explanation: 

List of two integers (1-based indices). 

Examples: 

Input: nums = [2,7,11,15], target = 9 
Output: [1,2] 
Explanation: 2 + 7 = 9. 
 

Input: nums = [1,2,3,4,4,9,56,90], target = 8 
Output: [4,5] 
Explanation: 4 + 4 = 8. 


### Approach
Describe your approach here...

### Pseudocode

Set left to 0, right to n-1  
While left < right:  
    If nums[left] + nums[right] == target:  
        Return [left+1, right+1]  
    If sum < target:  
        Increment left  
    Else:  
        Decrement right

### Time Complexity

O(n)

### Space Complexity

O(1)

