from typing import List

def sum_array_elements(arr: List[int]) -> int:
    total = 0
    for element in arr:
        total += element
    return total

class Solution:
    def sumArray(self, arr: list[int]) -> int:
        pass

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.sumArray([1,2,3]))          # Output: 6
    print(sol.sumArray([-5,10,-3]))       # Output: 2

