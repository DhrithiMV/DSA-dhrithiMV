# Top K Frequent Elements with Stability
**Topic:** Hashtables

**Type:** Home Challenge

Problem :

Given a non-empty list of integers nums and an integer k, return the k most frequent elements. 

Sort the result by: 

Frequency of elements (descending). 

If frequency ties, maintain the order of their first appearance in nums (stable by first occurrence). 

Examples 

Input: nums = [1][1][1][2][2][3], k = 2 

Output: [1][2] 

Explanation: 1 occurs 3 times, 2 occurs twice. 

Input: nums = [4][4][1][1][2][2], k = 3 

Output: [4][1][2] 

Explanation: All have frequency 2, returned in first occurrence order. 

Input: nums = [3][3][3][2][2][2][1][1], k = 2 

Output: [3][2] 

Explanation: Top two frequencies are 3 (for numbers 3 and 2). First occurrence 3 comes before 2. 

Input: nums = [5], k = 1 

Output: [5] 

Explanation: Single element. 

### Approach

Use a hash map (Counter) to count frequencies of all elements.  
To handle tie cases (same frequency), track the first occurrence index of each element.  
Sort by:
1. Frequency in descending order
2. First occurrence index in ascending order for stability.

Return top k elements after sorting.

### Pseudocode

Initialize Counter for frequencies and a dict for first occurrences  
For each number:
 If number not in first_occurrence, record its index  
Sort all unique numbers by (-frequency, first_occurrence)  
Return first k elements  

### Time Complexity

O(n log n) — due to sorting of unique elements  

### Space Complexity

O(n) — for frequency and index maps  
