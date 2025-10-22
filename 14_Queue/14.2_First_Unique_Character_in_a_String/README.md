# First Unique Character in a String
**Topic:** Queue

**Type:** In-Session

Problem :

Given a string s, find the first non-repeating character and return its index. If none exists, return -1. 

Examples: 

Input: s = "leetcode" 
 Output: 0 
 Explanation: The first unique character is 'l' at index 0. 

Input: s = "loveleetcode" 
 Output: 2 
 Explanation: First unique character is 'v' at index 2, since 'l' and 'o' repeat. 

Input: s = "aabb" 
 Output: -1 
 Explanation: All characters repeat. 

Input: s = "aabcd" 
 Output: 2 
 Explanation: 'b' is the first character appearing only once. 

Constraints: 

1 <= s.length <= 10^5 

s consists of lowercase English letters. 

### Approach
Describe your approach here...

### Pseudocode

Create empty count dictionary  
For each character in s:  
 Increment count of character  
For each index and character in s:  
 If count of character is 1:  
  Return index  
Return -1

### Time Complexity

O(n)

### Space Complexity

O(1) (since alphabet size is limited)

