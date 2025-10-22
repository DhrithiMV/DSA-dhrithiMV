# Trapping Rain Water
**Topic:** Lists with Two Pointer Techniques

**Type:** Home Challenge

Problem :

 Given a list of non-negative integers height representing an elevation map, compute how much water it can trap after raining. 

Input Explanation: 

height: List of non-negative integers. 

Output Explanation: 

Integer: total units of trapped water. 

Examples: 

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] 
Output: 6 
Explanation: Total trapped water is 6 units. 
 

Input: height = [4,2,0,3,2,5] 
Output: 9 
Explanation: Total trapped water is 9 units. 
 

### Approach
Describe your approach here...

### Pseudocode

Set left = 0, right = n-1, left_max = 0, right_max = 0, total = 0  
While left < right:  
    If height[left] < height[right]:  
        If height[left] >= left_max:  
            left_max = height[left]  
        Else:  
            total += left_max - height[left]  
        left += 1  
    Else:  
        If height[right] >= right_max:  
            right_max = height[right]  
        Else:  
            total += right_max - height[right]  
        right -= 1  
Return total

### Time Complexity

O(n)

### Space Complexity

O(1)

