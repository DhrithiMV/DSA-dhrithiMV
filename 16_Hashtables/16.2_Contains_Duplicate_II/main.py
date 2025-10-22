# Contains Duplicate II
# Topic: Hashtables
# Type: In-Session

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        return False

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))     # True (1 repeats within distance 3)
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))     # True (1 repeats within distance 1)
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False (repeats too far apart)
           
