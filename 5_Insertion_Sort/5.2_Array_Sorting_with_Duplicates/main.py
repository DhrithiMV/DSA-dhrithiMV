class Solution:
    def sortByParity(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] % 2 > key % 2:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortByParity([3,1,2,4]))
    print(sol.sortByParity([0,5,6,7]))
