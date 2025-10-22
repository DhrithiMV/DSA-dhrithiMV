from typing import List

def reverse_array_inplace(arr: List[int]) -> List[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxElement([3,7,2,9,5]))    # Output: 9
    print(sol.maxElement([-10,-5,-1]))    # Output: -1
