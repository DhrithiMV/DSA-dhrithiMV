# Check Prime Number
**Topic:** Space Complexity

**Type:** Home Challenge


Problem Statement: 

 Given an integer n, check if it is a prime number. 

Input Format: 

An integer n. 

Output Format: 

A boolean (true or false). 

Constraints: 

2 <= n <= 10^5 

Example: 

Input:  7   
Output: true   
  

### Approach
Describe your approach here...

### Pseudocode
function is_prime(n):
  // Handle cases for n <= 1, which are not prime.
  if n <= 1:
    return False
  
  // Handle cases for 2 and 3, which are prime.
  if n <= 3:
    return True
    
  // Handle cases divisible by 2 or 3, which are not prime.
  if n modulo 2 == 0 or n modulo 3 == 0:
    return False
  
  // Initialize a counter starting from 5.
  i = 5
  
  // Loop from 5 up to the square root of n.
  while i * i <= n:
    // Check for divisibility by i and i + 2.
    if n modulo i == 0 or n modulo (i + 2) == 0:
      return False
    
    // Increment the counter by 6 for the next pair of checks.
    i = i + 6
  
  // If no divisors were found, n is prime.
  return True


### Time Complexity
O(root n)

### Space Complexity
O(1)
