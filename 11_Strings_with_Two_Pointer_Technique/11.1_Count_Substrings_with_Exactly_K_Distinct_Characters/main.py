# Count Substrings with Exactly K Distinct Characters
# Topic: Strings with Two Pointer Technique
# Type: In-Session

class Solution:
    def substrCount(self, s: str, k: int) -> int:
        def atMostK(s, k):
            left = 0
            count = 0
            freq = {}
            for right in range(len(s)):
                freq[s[right]] = freq.get(s[right], 0) + 1
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                count += right - left + 1
            return count
        return atMostK(s, k) - atMostK(s, k - 1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.substrCount("pqpqs", 2))


# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.substrCount("pqpqs", 2)) 
