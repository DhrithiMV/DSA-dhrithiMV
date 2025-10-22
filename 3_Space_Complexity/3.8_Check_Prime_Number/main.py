def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True
class Solution:
    def isPrime(self, n: int) -> bool:
        pass

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPrime(7))                 # Output: True
    print(sol.isPrime(10))                # Output: False
