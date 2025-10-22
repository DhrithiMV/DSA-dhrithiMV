# Quadratic Time (O(n²))
**Topic:** Time & Space Complexity
**Type:** Home Challenge
Problem 5 — Quadratic Time (O(n²)) 
Print All Pairs in Array 
Statement: Given an array, print all pairs of numbers. 
Constraints: 1 ≤ n ≤ 1000 
Time Complexity: O(n²) 
Space Complexity: O(1) 
Test Cases: 
Input: [1,2,3] → Output: (1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3) 
Input: [5,6] → Output: (5,5),(5,6),(6,5),(6,6) 
Input: [7] → Output: (7,7) 
### Approach
Use two nested loops to print every possible pair from the array.
### Pseudocode
```
FUNCTION printPairs(arr):
    FOR i FROM 0 TO n-1:
        FOR j FROM 0 TO n-1:
            PRINT (arr[i], arr[j])
```
### Time Complexity
O(n²)
### Space Complexity
O(1)
