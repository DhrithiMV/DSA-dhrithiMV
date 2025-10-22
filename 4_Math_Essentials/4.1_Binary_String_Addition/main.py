class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            sum_val = carry
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            if j >= 0:
                sum_val += int(b[j])
                j -= 1
            res = str(sum_val % 2) + res
            carry = sum_val // 2
        return res

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary("11", "1"))      # Output: "100"
    print(sol.addBinary("1010", "1011")) # Output: "10101"
