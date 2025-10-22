# Reverse First K Elements of a Queue
**Topic:** Deque

**Type:** In-Session

Problem :

Given a queue of integers, reverse the order of the first k elements, leaving the rest of the queue unchanged. 

Input and Output Explanation 

Input: Two inputs are given: a list representing the queue elements in order, and an integer k indicating how many elements from the front to reverse. 

Output: Return a new list with the first k elements reversed and remaining elements as in original order. 

Examples 

Input: queue = [^1][^2][^3][^4][^5], k = 3 
 Output: [^3][^2][^1][^4][^5] 
 Explanation: The first three elements 1, 2, 3 are reversed to 3, 2, 1, rest unchanged. 

Input: queue = [^4][^8][^6][^7], k = 2 
 Output: [^8][^4][^6][^7] 
 Explanation: Only first two elements swapped. 

Input: queue = [^9][^5][^2][^1], k = 4 
 Output: [^1][^2][^5][^9] 
 Explanation: All elements reversed. 

### Approach
Describe your approach here...

### Pseudocode

If k is invalid, return original queue  
Push first k elements of queue into stack  
Pop all elements from stack and enqueue back into queue  
Move remaining (n - k) elements of queue from front to back  
Return updated queue

### Example

Input: q = [1, 2, 3, 4, 5], k = 3  
Output: [3, 2, 1, 4, 5]

### Time Complexity

O(n)

### Space Complexity

O(k)

