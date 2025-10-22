def factorial(n: int) -> int:
    if n < 0:
        return None # type: ignore
    elif n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.factorial(5))               # Output: 120
    print(sol.factorial(0))               # Output: 1

