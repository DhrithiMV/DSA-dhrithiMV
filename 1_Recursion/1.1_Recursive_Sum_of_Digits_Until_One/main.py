class Solution:
    def recursiveDigitSum(self, n: int) -> int:
        if n < 10:
            return n
        sum_of_digits = 0
        while n > 0:
            sum_of_digits += n % 10
            n //= 10
        return self.recursiveDigitSum(sum_of_digits)


sol = Solution()
print(sol.recursiveDigitSum(9875)) 
print(sol.recursiveDigitSum(1234))  
print(sol.recursiveDigitSum(5))     
