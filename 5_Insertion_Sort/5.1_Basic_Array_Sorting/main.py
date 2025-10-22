from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        
        return nums



# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.insertionSort([5,2,3,1]))        # Output: [1,2,3,5]
    print(sol.insertionSort([10,7,8,9,1]))    # Output: [1,7,8,9,10]
