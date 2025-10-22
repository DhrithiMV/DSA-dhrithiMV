# Longest Palindromic Substring using Manacher's Algorithm
# Topic: Strings with Two Pointer Technique
# Type: Home Challenge

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = max_len = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))


# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abacdfgdcaba"))  
    print(sol.longestPalindrome("bananas"))       
