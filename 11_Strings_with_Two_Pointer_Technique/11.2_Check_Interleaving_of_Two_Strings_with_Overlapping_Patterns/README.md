# Check Interleaving of Two Strings with Overlapping Patterns
**Topic:** Strings with Two Pointer Technique

**Type:** Home Challenge

Problem :

 Given three strings s1, s2, and s3, check if s3 is formed by an interleaving of s1 and s2. Characters in s1 and s2 can appear multiple times, and overlapping repeated patterns should be managed using an optimized two-pointer strategy. Input lengths may be large, demanding linear or near-linear time complexity. 

Example: 
 Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" 
 Output: true 

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" 
 Output: false 

Constraints: 

1≤s1.length,s2.length≤105 

s3.length=s1.length+s2.length 

### Approach
Describe your approach here...

### Pseudocode
### Pseudocode

If len(s1) + len(s2) != len(s3):  
 Return False  
Initialize dp of size len(s2)+1 with False  
Set dp[0] = True  
For j = 1 to len(s2):  
 dp[j] = dp[j-1] and s2[j-1] == s3[j-1]  
For i = 1 to len(s1):  
 dp[0] = dp[0] and s1[i-1] == s3[i-1]  
 For j = 1 to len(s2):  
  dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])  
Return dp[-1]

### Time Complexity

O(mn) where m = len(s1), n = len(s2)

### Space Complexity

O(n)
