
### Reverse Nodes in k-Group 

**Topic:** Linked List

**Type:** Home Challenge

Problem :

Given a linked list, reverse the nodes in groups of size k and return its modified list. If the number of nodes is not a multiple of k, leave the last nodes as is. 

Detailed Explanation 

Process the list in chunks of k nodes, reversing the nodes in each chunk. The last remaining chunk with fewer than k nodes remains unchanged. 

Examples 

Example 1: 
 Input: [1->2->3->4->5], k=2 
 Output: [2->1->4->3->5] 
 Explanation: The first two nodes are reversed, second two nodes reversed, last node remains. 
 

### Approach
Describe your approach here...

### Pseudocode

Initialize a min-heap  
Push first node of each list to heap  
While heap is not empty:  
    Pop smallest node  
    Add node to merged list  
    If node.next exists:  
        Push node.next to heap  
Return merged list

### Time Complexity

O(N log k), where N = total number of nodes, k = number of lists

### Space Complexity

O(k)
