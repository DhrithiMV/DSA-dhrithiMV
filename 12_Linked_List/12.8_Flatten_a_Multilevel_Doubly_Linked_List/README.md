
# Flatten a Multilevel Doubly Linked List 

**Topic:** Linked List

**Type:** Home Challenge

Problem :

Given a doubly linked list where a node may have a child pointer to another doubly linked list, flatten the list into a single-level doubly linked list. 

Detailed Explanation 

Traverse nodes and every time a node has a child, append the child list into the main list by adjusting pointers. Recursively flatten child lists. Ensure the prev, next, and child pointers are updated to maintain the doubly linked structure without nesting. 

Examples 

Example: 
 Input: 1 <-> 2 <-> 3, where 2 has child 4 <-> 5 
 Output: 1 <-> 2 <-> 4 <-> 5 <-> 3 


 

### Approach
Describe your approach here...

### Pseudocode

Initialize dummy node before head  
While true:  
    Set kth = prev  
    Move kth k steps  
    If kth is None: break  
    Reverse group from prev.next to kth  
    Update prev for next group  
Return dummy.next

### Time Complexity

O(n)

### Space Complexity

O(1)
