class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 1
        length = 1
        
        while remainder % k != 0:
            remainder = (remainder * 10 + 1) % k
            length += 1
            if length > k:
                return -1
                
        return length

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestRepunitDivByK(1))  # Output: 1
    print(sol.smallestRepunitDivByK(2))  # Output: -1
    print(sol.smallestRepunitDivByK(3))  # Output: 3
