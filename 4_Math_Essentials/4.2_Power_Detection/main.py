# Power Detection
# Topic: Math Essentials
# Type: In-Session

class Solution:  
    def isPowerOfTwo(self, n: int) -> bool:
        class Solution:
            if n <= 0:
                return False
            return (n & (n - 1)) == 0
        

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(1))   # Output: True
    print(sol.isPowerOfTwo(16))  # Output: True
    print(sol.isPowerOfTwo(3))   # Output: False
