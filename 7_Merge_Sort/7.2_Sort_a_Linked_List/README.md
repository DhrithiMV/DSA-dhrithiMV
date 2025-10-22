# Sort a Linked List
**Topic:** Merge Sort
**Type:** Home Challenge
Problem :
Given the head of a singly linked list, return the list after sorting it in ascending order. 
 You must use Merge Sort because of the linked list constraints (no random access). 
 Example 
Input: 
head = [4, 2, 1, 3] 
  
Output: [1, 2, 3, 4] 
  
 
Constraints 
The number of nodes in the list is in the range [0, 5 * 10^4]. 
-10^5 <= Node.val <= 10^5 
 
### Approach
Use Merge Sort on the linked list. Find midpoint with fast/slow pointers, recursively sort left and right halves, then merge two sorted lists with a standard merge procedure.

### Pseudocode
```
FUNCTION sortList(head):
    IF head is None OR head.next is None:
        RETURN head
    mid = findMid(head)
    left = sortList(head)
    right = sortList(mid)
    RETURN merge(left, right)

FUNCTION findMid(head):
    slow, fast = head, head.next
    WHILE fast is not None AND fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    RETURN mid

FUNCTION merge(l1, l2):
    dummy = ListNode(-1)
    tail = dummy
    WHILE l1 != None AND l2 != None:
        IF l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        ELSE:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    Attach remaining nodes
    RETURN dummy.next
```

### Time Complexity
O(n log n)

### Space Complexity
O(log n) due to recursion stack
