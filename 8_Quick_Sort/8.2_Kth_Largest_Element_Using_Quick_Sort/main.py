class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, k)
    def quickSelect(self, arr, low, high, k):
        if low == high:
            return arr[low]
        pi = self.partition(arr, low, high)
        if pi == k:
            return arr[pi]
        elif pi > k:
            return self.quickSelect(arr, low, pi - 1, k)
        else:
            return self.quickSelect(arr, pi + 1, high, k)
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
