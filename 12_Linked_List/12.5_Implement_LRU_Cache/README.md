
# Implement LRU Cache

**Topic:** Linked List

**Type:** Home Challenge


Problem :


Design a data structure representing an LRU (Least Recently Used) cache. It should support the following operations in O(1) time: 

get(key): Return the value of the key if it exists, else -1. 

put(key, value): Insert or update the value of the key. If the cache reaches capacity, it should evict the least recently used item before inserting. 

Use a combination of a hashmap for O(1) access and a doubly linked list to track usage order. 

Detailed Explanation 

Least Recently Used (LRU) cache maintains the most recently accessed items easily accessible and removes the least accessed ones on capacity overflow. Doubly linked list nodes represent cache entries, with the head as the most recent and the tail as least. The hashmap maps keys to nodes in the list, making insertions, accesses, and removals efficient in O(1). 

When an item is accessed, it is moved to the front of the list. If capacity is reached on inserting a new item, the tail node (least recent) is removed. 

Input and Output Format 

Input: Series of operations (put, get) with keys and values 

Output: Values returned by get operations 

Examples 

Example 1: 
 Input: 

put(1, 1) 
 put(2, 2) 
 get(1) -> returns 1 
 put(3, 3)  # evicts key 2  
get(2) -> returns -1 (not found) 
 put(4, 4)  # evicts key 1 
 get(1) -> returns -1 (not found) 
 get(3) -> returns 3 
 get(4) -> returns 4 

 

### Approach
Describe your approach here...

### Pseudocode

Initialize dummy and tail pointers  
While both lists are not empty:  
    If l1.val < l2.val:  
        tail.next = l1  
        l1 = l1.next  
    Else:  
        tail.next = l2  
        l2 = l2.next  
    Move tail to tail.next  
Attach remaining nodes from non-empty list  
Return dummy.next

### Time Complexity

O(n + m) where n, m are the lengths of l1 and l2

### Space Complexity

O(1)
