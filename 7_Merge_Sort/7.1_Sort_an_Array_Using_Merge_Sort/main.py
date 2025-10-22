# Sort an Array Using Merge Sort
# Topic: Merge Sort
# Type: In-Session
from typing import List
class Solution:
    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left, right)
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeSort([5,2,3,1]))      
    print(sol.mergeSort([10,7,8,9,1]))   
