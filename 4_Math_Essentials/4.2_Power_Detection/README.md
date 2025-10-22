# Power Detection
**Topic:** Math Essentials

**Type:** In-Session

Problem : 

Given an integer n, return true if it is a power of two. Otherwise, return false. 

An integer n is a power of two, if there exists an integer x such that n == 2^x. 

Example 1: 

Input: n = 1 
Output: true 
Explanation: 2^0 = 1 
 

Example 2: 

Input: n = 16 
Output: true 
Explanation: 2^4 = 16 
 

Example 3: 

Input: n = 3 
Output: false 
 

Constraints: 

-2^31 <= n <= 2^31 - 1 

### Approach
Describe your approach here...

### Pseudocode
function isPowerOfTwo(n):
  // A number must be positive to be a power of two.
  if n is less than or equal to 0:
    return false
  
  // A number that is a power of two has only one bit set in its binary representation.
  // The expression (n & (n - 1)) clears the least significant bit that is set to 1.
  // If n is a power of two, it has only one bit set.
  // Subtracting 1 from it will flip that bit to 0 and all trailing 0s to 1s.
  // For example: 8 (1000) & 7 (0111) = 0.
  // The bitwise AND operation will result in 0 if and only if n was a power of two.
  return (n bitwise_AND (n - 1)) is equal to 0

### Time Complexity
O(1)

### Space Complexity
O(1)
