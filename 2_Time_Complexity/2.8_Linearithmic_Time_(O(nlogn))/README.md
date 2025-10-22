# Linearithmic Time (O(nlogn))
**Topic:** Time & Space Complexity
**Type:** Home Challenge
Linearithmic Time (O(n log n)) 
Statement: Given a number n, repeatedly halve it until 1. At each step, print numbers from 1 to current n. 
Constraints: 1 ≤ n ≤ 1000 
Time Complexity: O(n log n) 
Space Complexity: O(1) 
Test Cases: 
Input: n=8 → Output: 
1 2 3 4 5 6 7 8 
1 2 3 4 
1 2 
1 
  
Input: n=5 → Output: 
1 2 3 4 5 
1 2 
1 
  
Input: n=1 → Output: 1 

### Approach
Use merge sort to recursively divide the array and merge sorted halves. Each merge step combines two sorted arrays into one, leading to O(n log n) time.
### Pseudocode
FUNCTION mergeSort(arr):
    IF length(arr) > 1:
        mid = length(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge left and right into arr
### Time Complexity
O(n log n)
### Space Complexity
O(n)
