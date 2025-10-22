# Find the Array K-th Selection Sort Swap
# Topic: Selection Sort
# Type: Home Challenge
class Solution:
    def kthSwapSelectionSort(self, nums, k):
        swaps = 0
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
                swaps += 1
                if swaps == k:
                    return nums
        return nums
# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.kthSwapSelectionSort([64,25,12,22,11], 2)) 
