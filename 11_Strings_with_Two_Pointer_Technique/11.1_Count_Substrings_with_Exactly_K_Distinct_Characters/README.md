# Count Substrings with Exactly K Distinct Characters
**Topic:** Strings with Two Pointer Technique

**Type:** In-Session

Problem :

 Given a string s and an integer k, find the number of substrings that contain exactly k distinct characters. Use a two-pointer sliding window technique to efficiently count such substrings. 

Example: 
 Input: s = "pqpqs", k = 2 
 Output: 7 
 Explanation: The substrings with exactly 2 distinct characters are: "pq", "pqp", "qp", "qpq", "pq", "qs", "s". 

Constraints: 
 1 ≤ s.length ≤ 10^5 
 s consists of lowercase English letters. 
 1 ≤ k ≤ 26 

### Approach
Describe your approach here...

### Pseudocode

Define atMostK(s, k):
    Initialize left = 0, count = 0, empty freq dictionary
    For right from 0 to n-1:
        Increment freq[s[right]] by 1
        While number of distinct keys in freq > k:
            Decrement freq[s[left]] by 1
            If freq[s[left]] == 0:
                Remove s[left] from freq
            Increment left by 1
        Increment count by right - left + 1
    Return count

Return atMostK(s, k) - atMostK(s, k-1)

### Time Complexity

O(n)

### Space Complexity

O(k)

