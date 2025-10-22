# Shortest Subarray With Sum At Least K
# Topic: Deque
# Type: Home Challenge

from collections import deque
from typing import List
import itertools

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = list(itertools.accumulate(nums, initial=0))
        dq = deque()
        min_len = n + 1

        for i in range(n + 1):
            # Check if current prefix - smallest prefix in deque >= k
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())

            # Maintain increasing order in prefix sums
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_len if min_len <= n else -1

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestSubarray([2, -1, 2], 3))             # 3
    print(sol.shortestSubarray([1, 2], 4))                  # -1
    print(sol.shortestSubarray([1, 2, 3, 4, 5], 11))        # 3
    print(sol.shortestSubarray([84, -37, 32, 40, 95], 167)) # 3
