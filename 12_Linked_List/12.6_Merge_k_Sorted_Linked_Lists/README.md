
# Merge k Sorted Linked Lists 

**Topic:** Linked List

**Type:** Home Challenge

Problem :


Given an array of k sorted linked lists, merge them into one sorted linked list. 

Detailed Explanation 

You’ll merge multiple sorted lists while maintaining sorted order. An efficient method is to use: 

Min-heap: Push the first node of each list into a priority queue, extract the smallest node, then push its successor. 

Or Divide and conquer: Merge lists pairwise, reducing the number of lists until only one remains. 

Examples 

Example 1: 
 Input: [[1->4->5], [1->3->4], [2->6]] 
 Output: 1->1->2->3->4->4->5->6 

Explanation: All lists merged in ascending order. 

 

### Approach
Describe your approach here...

### Pseudocode
```
Write your pseudocode here...
```

### Time Complexity
- 

### Space Complexity
- 
