# Delivering Boxes from Storage to Ports
# Topic: Queue
# Type: Home Challenge

from typing import List
from collections import deque

def boxDelivering(boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
    n = len(boxes)
    ws = [0] * (n + 1)
    cs = [0] * (n + 1)

    # Prefix sums for weights and port changes
    for i in range(n):
        p, w = boxes[i]
        ws[i + 1] = ws[i] + w
        if i > 0:
            cs[i + 1] = cs[i] + (1 if boxes[i][0] != boxes[i - 1][0] else 0)

    dp = [0] * (n + 1)
    dq = deque([0])

    for i in range(1, n + 1):
        # Maintain valid deque window
        while dq and (i - dq[0] > maxBoxes or ws[i] - ws[dq[0]] > maxWeight):
            dq.popleft()

        dp[i] = cs[i - 1] - cs[dq[0]] + dp[dq[0]] + 2

        # Maintain deque monotonicity
        if i != n:
            while dq and dp[dq[-1]] - cs[dq[-1]] >= dp[i] - cs[i]:
                dq.pop()
            dq.append(i)

    return dp[n]

# Demo
if __name__ == "__main__":
    boxes = [[1,1],[2,1],[1,1]]
    print(boxDelivering(boxes, 2, 3, 3))  # Expected output: 4

    boxes2 = [[1,2],[3,3],[3,1],[3,1],[2,4]]
    print(boxDelivering(boxes2, 3, 3, 6)) # Expected output: 6
