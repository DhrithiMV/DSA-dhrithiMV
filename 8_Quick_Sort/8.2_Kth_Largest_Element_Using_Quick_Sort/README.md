### Approach
Use Quick Select, a partition-based selection algorithm. Partition the array recursively; if kth largest is at the pivot, return. Otherwise, repeat search on left or right partition based on k.

### Pseudocode
FUNCTION findKthLargest(nums, k):
    k = length(nums) - k
    RETURN quickSelect(nums, 0, length(nums)-1, k)

FUNCTION quickSelect(arr, low, high, k):
    IF low == high:
        RETURN arr[low]
    pi = partition(arr, low, high)
    IF pi == k:
        RETURN arr[pi]
    ELSE IF pi > k:
        RETURN quickSelect(arr, low, pi - 1, k)
    ELSE:
        RETURN quickSelect(arr, pi + 1, high, k)

FUNCTION partition(arr, low, high):
    pivot = arr[high]
    i = low
    FOR j FROM low TO high-1:
        IF arr[j] <= pivot:
            SWAP arr[i], arr[j]
            i += 1
    SWAP arr[i], arr[high]
    RETURN i

### Time Complexity
O(n^2) worst-case, O(n) average

### Space Complexity
O(1)
