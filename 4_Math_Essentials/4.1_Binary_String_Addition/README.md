# Binary String Addition
**Topic:** Math Essentials

**Type:** In-Session

Problem Statement :

Given two binary strings a and b, return their sum as a binary string. 

Example 1: 

Input: a = "11", b = "1" 
Output: "100" 
 

Example 2: 

Input: a = "1010", b = "1011" 
Output: "10101" 
 

Constraints: 

1 <= a.length, b.length <= 10^4 

a and b consist only of '0' or '1' characters 

Each string does not contain leading zeros except for the zero itself 

 

 

### Approach
Describe your approach here...

### Pseudocode
function addBinary(a, b):
  // Initialize an empty string to store the result.
  res = ""
  
  // Initialize two pointers, 'i' and 'j', to the last character of each string.
  i = length(a) - 1
  j = length(b) - 1
  
  // Initialize a carry variable to 0.
  carry = 0
  
  // Loop until both strings are fully traversed and there is no carry.
  while i >= 0 or j >= 0 or carry is not 0:
    // Initialize the current sum with the value of the carry.
    sum_val = carry
    
    // Add the current bit of string 'a' if 'i' is still in bounds.
    if i >= 0:
      sum_val = sum_val + integer(a[i])
      i = i - 1
      
    // Add the current bit of string 'b' if 'j' is still in bounds.
    if j >= 0:
      sum_val = sum_val + integer(b[j])
      j = j - 1
      
    // Calculate the current bit of the result (sum_val modulo 2).
    // Prepend it to the result string.
    res = string(sum_val modulo 2) + res
    
    // Calculate the carry for the next position (sum_val integer_division 2).
    carry = sum_val integer_division 2
    
  // Return the final result string.
  return res


### Time Complexity
O(max(len(a),len(b)))
### Space Complexity
O(max(len(a),len(b)))
