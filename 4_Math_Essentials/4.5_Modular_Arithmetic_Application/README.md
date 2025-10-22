# Modular Arithmetic Application
**Topic:** Math Essentials

**Type:** Home Challenge

Problem :

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1. 

Return the length of n. If there is no such n, return -1. 

Note: n may not fit in a 64-bit signed integer. 

Example 1: 

Input: k = 1 
Output: 1 
Explanation: The smallest answer is n = 1, which has length 1. 
 

Example 2: 

Input: k = 2 
Output: -1 
Explanation: There is no such positive integer n divisible by 2. 
 

Example 3: 

Input: k = 3 
Output: 3 
Explanation: The smallest answer is n = 111, which has length 3. 
 

Constraints: 

1 <= k <= 10^5

### Approach
Describe your approach here...

### Pseudocode
function smallestRepunitDivByK(k):
  // Check the edge cases.
  // If k is divisible by 2 or 5, no repunit (a number made of only 1s) can be divisible by k.
  // This is because a repunit is always an odd number and does not end in 0 or 5.
  if k modulo 2 == 0 or k modulo 5 == 0:
    return -1
    
  // Initialize 'remainder' to 1, representing the repunit '1'.
  remainder = 1
  // Initialize 'length' to 1, representing the length of the repunit '1'.
  length = 1
  
  // Loop until the remainder is 0, which indicates divisibility by k.
  while remainder modulo k is not 0:
    // Update the remainder by appending a '1'.
    // The next repunit is (current_repunit * 10 + 1).
    // Using the properties of modular arithmetic, we can update the remainder incrementally:
    // (r * 10 + 1) % k
    remainder = (remainder * 10 + 1) modulo k
    
    // Increment the length of the repunit.
    length = length + 1
    
    // If the length exceeds k, it means a remainder of 0 was never found,
    // and a cycle has been detected. This is guaranteed by the Pigeonhole Principle.
    if length > k:
      return -1
      
  // If the loop terminates, a repunit divisible by k was found.
  // Return the length of that repunit.
  return length


### Time Complexity
O(k)

### Space Complexity
O(1)
