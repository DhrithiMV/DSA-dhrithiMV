# Subarray with Sum Closest to Target
# Topic: Lists with Two Pointer Techniques
# Type: Home Challenge

class Solution:
    def closestPair(self, nums, target):
        left, right = 0, len(nums) - 1
        closest = float('inf')
        ans = [left, right]
        while left < right:
            curr_sum = nums[left] + nums[right]
            if abs(curr_sum - target) < abs(closest - target):
                closest = curr_sum
                ans = [left, right]
            if curr_sum < target:
                left += 1
            else:
                right -= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.closestPair([-7,-3,2,5,10], 6))
    print(sol.closestPair([1,3,5,8,12], 16))
    print(sol.closestPair([-10,-5,-2,1], -9))

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.closestPair([-7,-3,2,5,10], 6))     
    print(sol.closestPair([1,3,5,8,12], 16))      
    print(sol.closestPair([-10,-5,-2,1], -9))   

