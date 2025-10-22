# Top K Frequent Elements with Stability
# Topic: Hashtables
# Type: Home Challenge

from typing import List
from collections import defaultdict, Counter

class Solution:
    def topKFrequentStable(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # Count frequencies
        first_occurrence = {}
        
        # Record first appearance for stability
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i

        # Sort by: frequency (descending) THEN first appearance (ascending)
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], first_occurrence[x[0]]))

        # Extract top k elements
        return [num for num, count in sorted_items[:k]]

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequentStable([1, 1, 1, 2, 2, 3], 2))      # [1, 2]
    print(sol.topKFrequentStable([4, 4, 1, 1, 2, 2], 3))      # [4, 1, 2]
    print(sol.topKFrequentStable([3, 3, 3, 2, 2, 2, 1, 1], 2))# [3, 2]
    print(sol.topKFrequentStable([5], 1))                     # [5]
          
