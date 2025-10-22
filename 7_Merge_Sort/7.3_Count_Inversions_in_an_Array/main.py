# Count Inversions in an Array
# Topic: Merge Sort
# Type: Home Challenge
from typing import List
class Solution:
    def countInversions(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = self.countInversions(arr[:mid])
        right, inv_right = self.countInversions(arr[mid:])
        merged, inv_merge = self.merge_and_count(left, right)
        return merged, inv_left + inv_right + inv_merge
    def merge_and_count(self, left, right):
        result = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv_count += len(left) - i
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv_count
# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.countInversions([2,4,1,3,5]))  
    print(sol.countInversions([5,4,3,2,1]))  
