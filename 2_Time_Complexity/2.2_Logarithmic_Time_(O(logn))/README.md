# Logarithmic Time (O(logn))
**Topic:** Time & Space Complexity
**Type:** In-Session
Statement: Given a number n, divide it by 2 until it becomes 1. Print the number of steps. 
Constraints: 1 ≤ n ≤ 10^9 
Time Complexity: O(log n) 
Space Complexity: O(1) 
Test Cases: 
Input: n=16 → Output: 4 
Input: n=8 → Output: 3 
Input: n=1 → Output: 0 
Input: n=100 → Output: 6 
### Approach
Keep dividing n by 2 and count the number of steps until reaching 1.
### Pseudocode
```
FUNCTION countDivisions(n):
    steps = 0
    WHILE n > 1:
        n = n // 2
        steps += 1
    RETURN steps
```
### Time Complexity
O(log n)
### Space Complexity
O(1)
