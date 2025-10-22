# Subarray Sum Equals K with Length Constraints
# Topic: Hashtables
# Type: Home Challenge

from typing import List
from collections import defaultdict, deque
import itertools

class Solution:
    def subarraySumWithLengthConstraints(self, nums: List[int], k: int, m: int, n: int) -> int:
        prefix_sum = list(itertools.accumulate(nums, initial=0))
        prefix_map = defaultdict(int)
        dq = deque()
        count = 0

        for i in range(len(prefix_sum)):
            # Add eligible prefix sums whose length ≤ n
            if i - m >= 0:
                prefix_map[prefix_sum[i - m]] += 1
            if i - n - 1 >= 0:
                val = prefix_sum[i - n - 1]
                prefix_map[val] -= 1
                if prefix_map[val] == 0:
                    del prefix_map[val]

            if prefix_sum[i] - k in prefix_map:
                count += prefix_map[prefix_sum[i] - k]

        return count

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySumWithLengthConstraints([1, 1, 1], 2, 2, 2))           # 2
    print(sol.subarraySumWithLengthConstraints([1, 2, 3, 1], 3, 1, 2))       # 2
    print(sol.subarraySumWithLengthConstraints([2, 2, 2, 2], 4, 2, 3))       # 3
    print(sol.subarraySumWithLengthConstraints([1, -1, 1, -1], 0, 2, 4))     # 4

