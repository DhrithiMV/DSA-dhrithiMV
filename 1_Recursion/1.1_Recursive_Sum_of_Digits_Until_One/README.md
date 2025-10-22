# Recursive Sum of Digits Until One
**Topic:** Recursion

**Type:** In-Session


Problem Statement: 

 You are given an integer n. 

 Your task is to determine, using recursion, the single-digit result obtained by repeatedly summing the digits of n until only one digit remains. 

Example 1: 
Input: n = 9875 
 Output: 2 

Explanation: 
 9 + 8 + 7 + 5 = 29 
 2 + 9 = 11 
 1 + 1 = 2 

Example 2: 
Input: n = 1234 
 Output: 1 

Explanation: 
 1 + 2 + 3 + 4 = 10 
 1 + 0 = 1 


Example 3: 
Input: n = 5 
 Output: 5 
Explanation: Already a single digit. 

 

Constraints: 
0 ≤ n ≤ 10⁹ 

### Approach
Describe your approach here...

### Pseudocode
function recursiveDigitSum(n):
  // Base case: If the number has a single digit, return it
  if n < 10:
    return n

  // Recursive step: Otherwise, calculate the sum of the digits
  sum_of_digits = 0
  temp_n = n
  while temp_n > 0:
    sum_of_digits += temp_n % 10
    temp_n //= 10

  // Recursively call the function with the new sum
  return recursiveDigitSum(sum_of_digits)


### Time Complexity
(O(log n)) 

### Space Complexity
(O(log n)) 
