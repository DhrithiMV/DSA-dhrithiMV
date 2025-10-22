# Two Sum with Multiple Pairs
# Topic: Hashtables
# Type: Home Challenge

from typing import List
from collections import defaultdict

class Solution:
    def twoSumAllPairs(self, nums: List[int], target: int) -> List[List[int]]:
        seen = defaultdict(int)
        pairs = set()

        for num in nums:
            complement = target - num
            if seen[complement] > 0:
                # Always store smaller first to ensure uniqueness
                pairs.add(tuple(sorted((num, complement))))
            seen[num] += 1
        
        return [list(pair) for pair in pairs]

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSumAllPairs([1, 2, 3, 4, 3], 6))      # [[2,4], [3,3]]
    print(sol.twoSumAllPairs([2, 7, 11, 15], 9))       # [[2,7]]
    print(sol.twoSumAllPairs([3, 3, 3], 6))            # [[3,3]]
    print(sol.twoSumAllPairs([1, 5, 1, 5], 6))         # [[1,5]]
