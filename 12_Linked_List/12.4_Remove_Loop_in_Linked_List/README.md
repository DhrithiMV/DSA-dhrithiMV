# Remove Loop in Linked list

**Topic:** Linked List

**Type:** Home Challenge

Problem :


You are given the head of a singly linked list that may contain a cycle (loop). Your task is to detect whether a cycle exists, and if so, remove the loop by making the linked list linear again without removing any nodes. 

Detailed Explanation 

A cycle in a linked list occurs when a node's next pointer points back to a previously visited node instead of null, causing infinite traversal. 

To detect the cycle, Floyd’s Cycle-Finding Algorithm uses two pointers: 

Slow pointer moves 1 step at a time. 

Fast pointer moves 2 steps at a time. 

If these pointers ever meet, a cycle exists. 

To find the cycle start: 

Reset one pointer to the head. 

Move both pointers 1 step at a time. 

The node where they meet again is the start of the loop. 

To remove the loop, break the cycle by setting the previous node’s next pointer (which points to the start of the loop) to null. 

Input Format 

An array representing node values of the linked list. 

An integer pos representing the index (0-based) of the node where the last node points to form a loop; -1 means no loop. 

Output Format 

The linked list printed in order without any loops. 

 
Examples 

Example 1 

Input: 

List: [^1][^3][^4][^2] 

Loop position: 1 (last node points to node at index 1, value 3) 

Output: 

1 -> 3 -> 4 -> 2 -> None 

Explanation: 

The node with value 2 originally points back to node with value 3, forming a loop. 

After removal, 2 points to None, and the list ends normally. 

Example 2 

Input: 

List: [^1][^2][^3][^4] 

Loop position: -1 (no loop) 

Output: 

1 -> 2 -> 3 -> 4 -> None 

Explanation: 

No cycle exists, so the list remains unchanged. 

Example 3 

Input: 

List: [^5][^6][^7][^8] 

Loop position: 0 (last node points to first node) 

Output: 

5 -> 6 -> 7 -> 8 -> None 

Explanation: 

The last node loops back to the first node. 

This cycle is detected and removed by breaking the pointer, making list linear. 

### Approach
Describe your approach here...

### Pseudocode

Use slow and fast pointers to detect cycle  
If cycle not found: return  
Move slow to head, keep fast at meeting point  
Move both one step at a time until they meet (start of loop)  
Move fast forward until fast.next == slow  
Set fast.next to None to remove loop

### Time Complexity

O(n)

### Space Complexity

O(1)
