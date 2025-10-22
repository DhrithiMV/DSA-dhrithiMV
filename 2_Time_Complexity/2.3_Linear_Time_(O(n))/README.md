# Linear Time (O(n))
**Topic:** Time & Space Complexity
**Type:** In-Session
Sum of Array Elements 
Statement: Given an array, find the sum of its elements. 
Constraints: 1 ≤ n ≤ 10^5, -10^3 ≤ arr[i] ≤ 10^3 
Time Complexity: O(n) 
Space Complexity: O(1) 
Test Cases: 
Input: [2,4,6,8] → Output: 20 
Input: [1] → Output: 1 
Input: [-5,10,-3] → Output: 2 
Input: [0,0,0,0] → Output: 0 
### Approach
Initialize a sum variable to 0. Iterate through each array element and add to sum.
### Pseudocode
```
FUNCTION arraySum(arr):
    sum = 0
    FOR each number in arr:
        sum += number
    RETURN sum
```
### Time Complexity
O(n)
### Space Complexity
O(1)
