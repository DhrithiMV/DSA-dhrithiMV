# Power of Four
**Topic:** Recursion

**Type:** Home Challenge


Problem Statement: 

 Given an integer n, return true if it is a power of four. Otherwise, return false. 

An integer n is a power of four if there exists an integer x such that n == 4^x. 

 

Example 1: 

Input: n = 1 

 Output: true 

 Explanation: 4⁰ = 1 

 

Example 2: 

Input: n = 16 

 Output: true 

 Explanation: 4² = 16 

 

Example 3: 

Input: n = 8 

 Output: false 

 Explanation: Although 8 is a power of two, it is not a power of four. 

 

Example 4: 

Input: n = 0 

 Output: false 

 

Example 5: 

Input: n = -4 

 Output: false 

 

Constraints: 

−2³¹ ≤ n ≤ 2³¹ − 1 

### Approach
Describe your approach here...

### Pseudocode
function recursiveDigitSum(n):
  // Base case: If n is a single-digit number, return n.
  if n < 10:
    return n

  // Recursive step: Calculate the sum of the digits
  sum_of_digits = 0
  while n > 0:
    sum_of_digits = sum_of_digits + (n modulo 10)
    n = n integer_division 10

  // Recursively call the function with the new sum
  return recursiveDigitSum(sum_of_digits)


### Time Complexity
(O(logn))
### Space Complexity
(O(logn))
