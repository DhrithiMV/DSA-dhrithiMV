# Implement Stacks using Queues
**Topic:** Queue

**Type:** In-Session



Problem :

Implement a last-in-first-out (LIFO) stack using only two queues. Your stack should support these operations: push (add element to top), pop (remove element from top), top (retrieve element at top), and empty (check if stack is empty). You must simulate stack behavior using only the basic queue operations (enqueue, dequeue, peek, size, is empty). 

Examples: 

Input: 

 push(1) 
 push(2) 
 top()  # returns 2 
 pop()  # returns 2 
 empty() # returns false 
  
 

Explanation: After pushing 1 and 2, top returns 2 (the last pushed). Popping removes 2. The stack is not empty. 

Input: 

 push(5) 
 push(10) 
 pop()  # returns 10 
 pop()  # returns 5 
 empty() # returns true 
  
 

Explanation: Elements 5 and 10 pushed. pop() removes 10 first, then 5. Following all pops, stack is empty. 

  

  

  

Input: 

 empty() # true 
 push(3) 
 top()   # returns 3 
  
 

Explanation: Initially, stack is empty. After push(3), top returns 3. 

Input: 

 push(7) 
 push(8) 
 push(9) 
 top()   # returns 9 
 pop()   # returns 9 
 pop()   # returns 8 
 empty() # returns false 
  
 

Explanation: Push elements 7,8,9 one by one. Top returns the latest pushed 9. Subsequent pops remove 9 then 8. Stack still contains 7. 

Constraints: 

All operations will be valid (pop or top called only on non-empty stack). 

Values pushed are integers. 

Up to 100 operations. 

### Approach
Describe your approach here...

### Pseudocode

Define result as empty list  
Define dfs(node):  
 If node:  
  Append node.val to result  
  dfs(node.left)  
  dfs(node.right)  
Call dfs(root)  
Return result

### Time Complexity

O(n) (visit each node once)

### Space Complexity

O(n) (stack space in worst case)
