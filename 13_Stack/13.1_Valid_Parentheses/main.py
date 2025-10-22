# Valid Parentheses
# Topic: Stack
# Type: In-Session

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
    def pop(self):
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
    def top(self):
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        top_elem = self.q[0]
        self.q.append(self.q.popleft())
        return top_elem
    def empty(self):
        return not self.q

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())   # 2
    print(stack.pop())   # 2
    print(stack.empty()) # False

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))       
    print(sol.isValid("()[]{}"))   
    print(sol.isValid("(]"))        

