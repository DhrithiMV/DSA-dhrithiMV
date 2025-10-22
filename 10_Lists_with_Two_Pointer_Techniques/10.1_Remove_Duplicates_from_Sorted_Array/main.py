# Remove Duplicates from Sorted Array
# Topic: Lists with Two Pointer Techniques
# Type: In-Session

def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


# Demo
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    print(sol.removeDuplicates(nums))  
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))  
