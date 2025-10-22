# Longest Palindromic Substring using Manacher's Algorithm
**Topic:** Strings with Two Pointer Technique

**Type:** Home Challenge

Problem :

 Given a string s, find the longest palindromic substring. Due to the large constraints, implement Manacher’s Algorithm which runs in linear time O(n), instead of the naive two-pointer expansion approach. 

Example: 
 Input: "abacdfgdcaba" 
 Output: "aba" (Multiple valid outputs possible) 

Input: "bananas" 
 Output: "anana" 

Constraints: 

1≤s.length≤106 

s consists of ASCII characters. 

### Approach
Describe your approach here...

### Pseudocode

Initialize chars as empty set, left = 0, max_len = 0  
For right from 0 to n-1:  
    While s[right] in chars:  
        Remove s[left] from chars  
        Increment left  
    Add s[right] to chars  
    Update max_len as max(max_len, right-left+1)  
Return max_len

### Time Complexity

O(n)

### Space Complexity

O(n)
