# Factorial of a Number
**Topic:** Space Complexity

**Type:** Home Challenge

Problem Statement: 

 Given an integer n, return the factorial of n. 

Input Format: 

An integer n. 

Output Format: 

The factorial of n. 

Constraints: 

0 <= n <= 12 

Example: 

Input:  5   
Output: 120   
  

 

### Approach
Describe your approach here...

### Pseudocode
function factorial(n):
  // Handle the case of negative input.
  if n < 0:
    return None

  // Base case for the loop: factorial of 0 is 1.
  if n == 0:
    return 1
    
  // Initialize a variable to store the result.
  result = 1

  // Loop from 1 up to n (inclusive).
  for i from 1 to n:
    // Multiply the result by the current number in the loop.
    result = result * i
    
  // Return the final result.
  return result

### Time Complexity
O(n)

### Space Complexity
O(1)
