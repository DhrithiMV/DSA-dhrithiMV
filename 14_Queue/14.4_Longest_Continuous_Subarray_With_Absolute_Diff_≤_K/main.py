# Longest Continuous Subarray With Absolute Diff ≤ K
# Topic: Queue
# Type: Home Challenge

from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))      # 1
    print(rc.ping(100))    # 2
    print(rc.ping(3001))   # 3
    print(rc.ping(3002))   # 3

