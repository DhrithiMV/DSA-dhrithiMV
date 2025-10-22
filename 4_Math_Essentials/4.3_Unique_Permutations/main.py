from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to group duplicates together
        
        def backtrack(current_perm, remaining_nums):
            # Base case: if the current permutation is the same length as the original nums,
            # it is a complete permutation. Add it to the result list.
            if not remaining_nums:
                res.append(current_perm[:])
                return
            
            for i in range(len(remaining_nums)):
                # Skip duplicates: if the current element is the same as the previous one
                # and has not been used, skip it to avoid generating duplicate permutations.
                if i > 0 and remaining_nums[i] == remaining_nums[i-1]:
                    continue
                
                # Choose: select the current element.
                num = remaining_nums[i]
                new_remaining = remaining_nums[:i] + remaining_nums[i+1:]
                current_perm.append(num)
                
                # Recurse: continue building the permutation.
                backtrack(current_perm, new_remaining)
                
                # Backtrack: undo the choice to explore other options.
                current_perm.pop()
        
        backtrack([], nums)
        return res


# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))  # Output: [[1,1,2],[1,2,1],[2,1,1]]
    print(sol.permuteUnique([1,2,3]))  # Output: 6 unique permutations

