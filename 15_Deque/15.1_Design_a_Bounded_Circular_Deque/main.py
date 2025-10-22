# Design a Bounded Circular Deque
# Topic: Deque
# Type: In-Session

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.q = [0] * k
        self.size = 0
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Demo
if __name__ == "__main__":
    deque = MyCircularDeque(3)
    print(deque.insertLast(5))    # True
    print(deque.insertFront(3))   # True
    print(deque.getRear())        # 5
    print(deque.deleteLast())     # True
    print(deque.getFront())       # 3
    print(deque.isEmpty())
