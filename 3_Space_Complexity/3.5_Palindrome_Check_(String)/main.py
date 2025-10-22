def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("madam"))      # Output: True
    print(sol.isPalindrome("hello"))      # Output: False
