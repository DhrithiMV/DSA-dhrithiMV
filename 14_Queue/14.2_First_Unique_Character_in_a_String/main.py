# First Unique Character in a String
# Topic: Queue
# Type: In-Session

def firstUniqChar(s: str) -> int:
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

# Demo
if __name__ == "__main__":
    print(firstUniqChar("leetcode"))       # 0
    print(firstUniqChar("loveleetcode"))   # 2
    print(firstUniqChar("aabb"))           # -1
    
