# Fibonacci Number (Iterative)
**Topic:** Space Complexity

**Type:** Home Challenge

Problem Statement: 

 Given an integer n, return the n-th Fibonacci number (0-indexed). 

Input Format: 

An integer n. 

Output Format: 

The n-th Fibonacci number. 

Constraints: 

0 <= n <= 30 

Example: 

Input:  6   
Output: 8   
  

### Approach
Describe your approach here...

### Pseudocode
function fibonacci(n):
  // Handle the base cases for n=0 and n=1.
  if n is less than or equal to 1:
    return n

  // Initialize the first two Fibonacci numbers.
  a = 0
  b = 1

  // Iterate from 2 up to n.
  for i from 2 to n:
    // Calculate the next Fibonacci number by summing the previous two.
    // Update the values of a and b for the next iteration.
    temp = a + b
    a = b
    b = temp
    
  // Return the nth Fibonacci number.
  return b

### Time Complexity
O(n)

### Space Complexity
O(1) 
