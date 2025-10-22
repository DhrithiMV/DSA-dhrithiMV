# Exponential Time (O(2ⁿ))
# Topic: Time & Space Complexity
# Type: Home Challenge
class Solution:
    def allSubsets(self, arr: list[int]) -> list[list[int]]:
        pass

def generate_subsets(arr, index=0, subset=None):
    if subset is None:
        subset = []
    if index == len(arr):
        print(subset)
        return
    generate_subsets(arr, index + 1, subset)
    generate_subsets(arr, index + 1, subset + [arr[index]])

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.allSubsets([1,2]))      # Output: [], [1], [2], [1,2]
    print(sol.allSubsets([3]))        # Output: [], [3]
    print(sol.allSubsets([1,2,3]))    # Output: 8 subsets
