# Cubic Time (O(n³))
**Topic:** Time & Space Complexity
**Type:** Home Challenge
 Cubic Time (O(n³)) 
Statement: Given an array, print all triplets of numbers. 
Constraints: 1 ≤ n ≤ 50 
Time Complexity: O(n³) 
Space Complexity: O(1) 
Test Cases: 
Input: [1,2,3] → Output: (1,1,1)…(3,3,3) (27 triplets) 
Input: [4,5] → Output: (4,4,4)…(5,5,5) (8 triplets) 
Input: [9] → Output: (9,9,9) 
### Approach
Use three nested loops to print all possible triplets from the array.
### Pseudocode
```
FUNCTION printTriplets(arr):
    FOR i FROM 0 TO n-1:
        FOR j FROM 0 TO n-1:
            FOR k FROM 0 TO n-1:
                PRINT (arr[i], arr[j], arr[k])
```
### Time Complexity
O(n³)
### Space Complexity
O(1)
