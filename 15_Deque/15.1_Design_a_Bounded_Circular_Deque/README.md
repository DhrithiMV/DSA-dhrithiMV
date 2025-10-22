# Design a Bounded Circular Deque
**Topic:** Deque

**Type:** In-Session

Problem :

Design a circular double-ended queue (deque) of fixed size that supports insertion and deletion at both front and rear ends, retrieves the front and rear elements, and checks empty/full status while using a circular array. 

Input and Output Explanation 

Input: A sequence of method calls such as insertFront(value), insertLast(value), deleteFront(), deleteLast(), getFront(), getRear(), isEmpty(), and isFull(). 

Output: 

For insert/delete operations, output indicates True if successful, False otherwise. 

For retrieval methods (getFront, getRear), output is the element value or -1 if empty. 

For isEmpty and isFull, output is boolean. 

Examples 

Operations: 

insertLast(5), insertFront(3), getRear(), deleteLast(), getFront(), isEmpty() 
  
Output: 

True, True, 5, True, 3, False 

Explanation: Add 5 rear, add 3 front, rear is 5, delete last removes 5, front now 3, not empty. 


Operations: 

insertLast(2), insertLast(4), insertFront(7), isFull(), deleteFront(), getFront() 

Output: 

True, False, True, True, True, 2 
  
 

Explanation: Second insertLast(4) fails (full), insertFront(7) succeeds, isFull is True, delete front removes 7, front now 2. 

Operations: 

isEmpty(), insertFront(8), deleteFront(), isEmpty() 
  

Output: 

True, True, True, True 
  

Explanation: Starts empty, insert 8 front, delete front removes it, empty again. 

### Approach
Describe your approach here...
### Pseudocode

Initialize result list  
Define helper _inorder(node, res):  
 If node is None, return  
 _recurse left_  
 Append node value to res  
 _recurse right_  
Call _inorder(root, res)_  
Return res

### Time Complexity

O(n)

### Space Complexity

O(n) (recursive stack)

