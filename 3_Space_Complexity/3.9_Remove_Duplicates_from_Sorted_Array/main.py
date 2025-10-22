class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        write_idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_idx] = nums[i]
                write_idx += 1
        
        return write_idx

class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        pass

# Demo
if __name__ == '__main__':
    sol = Solution()
    arr = [1,1,2,2,3]
    length = sol.removeDuplicates(arr)
    print(length)                        # Output: 3
    print(arr[:length])                   # Output: [1,2,3]

