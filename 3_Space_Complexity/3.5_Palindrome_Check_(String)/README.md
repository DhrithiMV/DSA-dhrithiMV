# Palindrome Check (String)
**Topic:** Space Complexity

**Type:** Home Challenge



Problem Statement: 

 Given a string s, check if it is a palindrome. Return true if yes, otherwise false. 

Input Format: 

A string s. 

Output Format: 

A boolean (true or false). 

Constraints: 

1 <= |s| <= 10^5 

s consists of lowercase English letters. 

Example: 

Input:  "madam"   
Output: true   
  

 

 

 
### Approach
Describe your approach here...

### Pseudocode
function is_palindrome(s):
  // Reverse the input string 's' to create a new string, 'reversed_s'
  reversed_s = reverse(s)

  // Compare the original string 's' with the reversed string 'reversed_s'
  if s is equal to reversed_s:
    return true
  else:
    return false


### Time Complexity
O(n)

### Space Complexity
O(n)
