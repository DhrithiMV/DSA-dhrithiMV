# Sliding Window Maximum
# Topic: Deque
# Type: In-Session

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # will store indices
        res = []

        for i in range(len(nums)):
            # Remove elements out of current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Once we reach window size k, record max
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindow([1], 1))                        # [1]
