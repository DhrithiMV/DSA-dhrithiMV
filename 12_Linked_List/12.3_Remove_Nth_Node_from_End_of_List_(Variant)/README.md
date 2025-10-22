# Remove Nth Node from End of List (Variant)
**Topic:** Linked List

**Type:** Home Challenge

Problem :

 Given the head of a singly linked list, sort the list in ascending order. Due to large constraints and to achieve optimal performance, implement merge sort algorithm which runs in O(n log n) time with O(1) auxiliary space (excluding recursion stack). This tests algorithm design skills and requires sophisticated pointer manipulation including finding middle node, splitting lists, and merging sorted sublists. 

Example: 

 Input: [4, 2, 1, 3] 

 Output: [1, 2, 3, 4] 

 Explanation: The unsorted list is sorted in ascending order using merge sort technique. 

Input: [2, 1] 

 Output: [1, 2] 

 Explanation: The two elements are swapped to achieve sorted order. 

Input: [3, 3, 1, 2] 

 Output: [1, 2, 3, 3] 

 Explanation: Duplicates are preserved and the list is sorted. Both 3's maintain their relative positions. 

 

Input: [] 

 Output: [] 

 Explanation: An empty list is already sorted. 

Input: [10, -1, 5, 0] 

 Output: [-1, 0, 5, 10] 

 Explanation: The list contains negative numbers. After sorting, -1 is first, followed by 0, 5, and 10. 

Input: [100, 50, 50, 25] 

 Output: [25, 50, 50, 100] 

 Explanation: Multiple duplicates are handled correctly, with both 50's appearing in the middle. 

Input: [5] 

 Output: [5] 

 Explanation: A single-node list is already sorted. 

Constraints: 

0 ≤ n ≤ 50,000 (length of list) 

Node values are integers (can be positive, negative, or zero) 

Must achieve O(n log n) time complexity 

Target O(1) auxiliary space complexity 

### Approach
Describe your approach here...

### Pseudocode

Initialize dummy node before head  
Set fast and slow to dummy  
Move fast forward n steps  
While fast.next exists:  
 Move fast and slow forward by one  
Set slow.next = slow.next.next  
Return dummy.next

### Time Complexity

O(n)

### Space Complexity

O(1)

