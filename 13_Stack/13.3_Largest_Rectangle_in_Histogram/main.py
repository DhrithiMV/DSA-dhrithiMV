# Largest Rectangle in Histogram
# Topic: Stack
# Type: Home Challenge

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # -3
    ms.pop()
    print(ms.top())     # 0
    print(ms.getMin())  # -2

   

