# Reverse a Linked List
**Topic:** Linked List

**Type:** In-Session

Problem :

 Given the head of a singly linked list, reverse the list in-place and return the new head. This fundamental problem builds understanding of pointer manipulation and helps master both iterative and recursive approaches to linked list operations. 

Example: 

 Input: [1, 2, 3, 4, 5] 

 Output: [5, 4, 3, 2, 1] 

 Explanation: Each link is reversed. The original head (1) becomes the tail, and the original tail (5) becomes the new head. 

Input: [1, 2] 

 Output: [2, 1] 

 Explanation: With only two nodes, they simply swap positions. 

Input: [1] 

 Output: [1] 

 Explanation: A single node list is already reversed as there are no links to change. 

Input: [] 

 Output: [] 

 Explanation: An empty list remains empty after reversal. 

Input: [10, 20, 30] 

 Output: [30, 20, 10] 

 Explanation: The three-node list is reversed, making 30 the new head and 10 the new tail. 

Input: [5, 5, 5] 

 Output: [5, 5, 5] 

 Explanation: Even with duplicate values, the structure is reversed though the output appears identical. 

Constraints: 

0 ≤ n ≤ 5000 (number of nodes) 

Node values are integers 

Must reverse in-place with O(1) extra space for iterative approach 

### Approach
Describe your approach here...

### Pseudocode

Initialize prev = None, current = head  
While current is not None:  
    Set next_node = current.next  
    Set current.next = prev  
    Set prev = current  
    Set current = next_node  
Return prev

### Time Complexity

O(n)

### Space Complexity

O(1)

