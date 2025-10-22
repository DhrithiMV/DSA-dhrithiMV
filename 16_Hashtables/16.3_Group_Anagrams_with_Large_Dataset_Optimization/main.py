# Group Anagrams with Large Dataset Optimization
# Topic: Hashtables
# Type: Home Challenge

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagramsOptimized(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Create a fixed-size frequency tuple as the hash key
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            anagram_map[key].append(s)

        return list(anagram_map.values())

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagramsOptimized(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output example: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(sol.groupAnagramsOptimized([""]))
    # [['']]
    print(sol.groupAnagramsOptimized(["a"]))
    # [['a']]
             
