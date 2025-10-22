# Sort the Array Using Selection Sort
# Topic: Selection Sort
# Type: In-Session

class Solution:
    def selectionSort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.selectionSort([64,25,12,22,11]))  
    print(sol.selectionSort([5,1,4,2,8]))
