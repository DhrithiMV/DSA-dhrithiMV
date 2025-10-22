# Reverse First K Elements of a Queue
# Topic: Deque
# Type: In-Session

from collections import deque

class Solution:
    def reverseK(self, queue: list[int], k: int) -> list[int]:
        if k <= 0 or k > len(queue):
            return queue

        q = deque(queue)
        stack = []

        # Step 1: Push first k elements into stack
        for _ in range(k):
            stack.append(q.popleft())

        # Step 2: Pop back into queue (reversed order)
        while stack:
            q.append(stack.pop())

        # Step 3: Move remaining elements to back
        for _ in range(len(q) - k):
            q.append(q.popleft())

        return list(q)

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseK([4, 8, 6, 7], 2))   # Output: [8, 4, 6, 7]
    print(sol.reverseK([9, 5, 2, 1], 4))   # Output: [1, 2, 5, 9]
