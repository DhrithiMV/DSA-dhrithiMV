# First Negative Number in Every Window of Size K
# Topic: Deque
# Type: Home Challenge

from collections import deque
from typing import List

class Solution:
    def firstNegativeInWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            if nums[i] < 0:
                dq.append(i)

            # Remove elements out of current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Record the first negative number for each window
            if i >= k - 1:
                result.append(nums[dq[0]] if dq else 0)

        return result

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstNegativeInWindow([12, -1, -7, 8, -15, 30, 16, 28], 3))  # [-1, -1, -7, -15, -15, 0]
    print(sol.firstNegativeInWindow([1, 2, 3, 4], 2))                     # [0, 0, 0]
    print(sol.firstNegativeInWindow([-5, 2, -3, 1, 4], 2))                # [-5, -3, -3, 0]
