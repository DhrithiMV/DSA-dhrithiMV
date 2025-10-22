# Number of Recent Calls
# Topic: Queue
# Type: Home Challenge

from collections import deque

def maxSlidingWindow(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    dq = deque()
    res = []

    for i in range(n):
        # Remove indexes that are out of window
        if dq and dq[0] == i - k:
            dq.popleft()
        # Remove from dq all elements less than current nums[i]
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

if __name__ == "__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
    print(maxSlidingWindow([1], 1))                 # [1]

