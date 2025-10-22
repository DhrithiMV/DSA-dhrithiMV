from typing import List

def count_even_numbers(arr: List[int]) -> int:
    count = 0
    for number in arr:
        if number % 2 == 0:
            count += 1
    return count
# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.countEven([2,5,6,7,8]))     # Output: 3
    print(sol.countEven([1,3,5]))         # Output: 0
