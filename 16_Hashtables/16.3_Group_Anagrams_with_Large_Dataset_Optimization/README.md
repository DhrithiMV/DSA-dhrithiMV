# Group Anagrams with Large Dataset Optimization
**Topic:** Hashtables

**Type:** Home Challenge

Problem :

Given a very large list of strings (potentially millions), group all anagrams together efficiently. Anagrams are strings with the same frequency of characters but possibly different order. 

You are required to: 

Return a list of grouped anagrams. 

Optimize for both time and space complexity. 

Handle long strings and large input volumes. 

Examples 

Input: ["eat", "tea", "tan", "ate", "nat", "bat"] 

Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] 

Explanation: Grouped by anagram equivalence. 

Input: [""] 

Output: [[""]] 

Explanation: Single empty string forms one group. 

Input: ["a"] 

Output: [["a"]] 

Explanation: Single string forms one group. 

Input: Large input: many long strings with subtle differences. 

Output: Groups sorted internally; efficiency critical. 

### Approach
Describe your approach here...

### Pseudocode

Initialize prefix_sum = 0, count = 0  
Initialize hash map prefix_map with {0: 1}  
For each num in nums:  
 Add num to prefix_sum  
 If (prefix_sum - k) in prefix_map, increment count by prefix_map[prefix_sum - k]  
 Add prefix_sum to prefix_map  
Return count

### Example

nums = [1, 1, 1], k = 2  
prefix_sums: [1, 2, 3]  
Valid subarrays: [1,1] (twice) → count = 2  

### Time Complexity

O(n)

### Space Complexity

O(n)

