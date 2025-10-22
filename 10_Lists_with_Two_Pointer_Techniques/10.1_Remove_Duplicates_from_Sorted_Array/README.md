# Remove Duplicates from Sorted Array
**Topic:** Lists with Two Pointer Techniques

**Type:** In-Session


Problem :

 Given a sorted list of integers nums, remove duplicates in-place. Return the count of unique elements (the first k elements of nums will be the result). 

Input Explanation: 

nums: A sorted list of integers. 

Output Explanation: 

Integer count of unique elements (the first "count" elements in nums are unique). 

Examples: 

Input: nums = [1,1,2] 
Output: 2 
Explanation: Unique elements are [1,2]. 
 

Input: nums = [0,0,1,1,1,2,2,3,3,4] 
Output: 5 
Explanation: Unique elements are [0,1,2,3,4]. 
 

### Approach
Describe your approach here...

### Pseudocode
### Pseudocode

Set i to 0  
For j from 1 to n-1:
  If nums[j] != nums[i], increment i, set nums[i] = nums[j]  
Return i+1

### Time Complexity

O(n)

### Space Complexity

O(1)
