# Sort an Array Using Quick Sort
**Topic:** Quick Sort
**Type:** In-Session
Problem :
Implement Quick Sort to sort an integer array in ascending order.
Example:
Input:
nums = [5, 2, 3, 1]
Output:
[1, 2, 3, 5]
Input:
nums = [5, 1, 1, 2, 0, 0]
Output:
[0, 0, 1, 1, 2, 5]
Constraints:
1 ≤ nums.length ≤ 10^4
-10^5 ≤ nums[i] ≤ 10^5

### Approach
Quick Sort is a classic divide-and-conquer sorting algorithm. Select a pivot, partition the array into elements smaller/greater than the pivot, then recursively sort both partitions.

### Pseudocode
FUNCTION quickSort(arr, low, high):
    IF low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

FUNCTION partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    FOR j FROM low TO high - 1:
        IF arr[j] < pivot:
            i += 1
            SWAP arr[i] <-> arr[j]
    SWAP arr[i + 1] <-> arr[high]
    RETURN i + 1

### Time Complexity
O(n^2) worst-case, O(n log n) average-case

### Space Complexity
O(log n) recursion stack (average)
