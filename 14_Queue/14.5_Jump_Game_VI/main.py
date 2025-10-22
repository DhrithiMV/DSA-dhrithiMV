# Jump Game VI
# Topic: Queue
# Type: Home Challenge

from typing import List
from collections import deque

def maxResult(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dq = deque([0])
    
    for i in range(1, n):
        # Remove indices that are out of range
        while dq and dq[0] < i - k:
            dq.popleft()
        
        # dp[i] = max(dp[j]) + nums[i] where j in [i-k, i-1]
        dp[i] = dp[dq[0]] + nums[i]
        
        # Maintain deque in decreasing order of dp values
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        
        dq.append(i)
    
    return dp[n-1]

# Demo
if __name__ == "__main__":
    print(maxResult([1,-1,-2,4,-7,3], 2))   # 7
    print(maxResult([10,-5,-2,4,0,3], 3))   # 17


