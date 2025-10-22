# Basic Array Sorting
**Topic:** Insertion Sort

**Type:** In-Session

Easy: Basic Array Sorting 

Sort an Array Given an array of integers nums, sort the array in ascending order using insertion sort and return it. 

Start with the first element as the sorted portion. 

For each subsequent element, insert it into its correct position in the sorted portion by shifting larger elements right. This is a foundational problem for mastering insertion sort’s loop invariants and array shifts, akin to sorting small datasets in a Django API endpoint. Constraints: 

1 ≤ nums.length ≤ 5 × 10^4 

-10^9 ≤ nums[i] ≤ 10^9 Example: 

Input: nums = [5,2,3,1] 

Output: [1,2,3,5] Why It Fits: Pure insertion sort on arrays, ideal for practicing iterative shifts and understanding best-case (O(n) for nearly sorted) vs. worst-case (O(n²)) performance. 

 

### Approach
Describe your approach here...

### Pseudocode
function sortArray(nums):
  // Start iterating from the second element (index 1) to the end of the array.
  for i from 1 to length(nums) - 1:
    // Store the current element in a variable 'key'.
    key = nums[i]
    // Initialize a pointer 'j' to the element just before the 'key'.
    j = i - 1
    
    // While 'j' is a valid index and the element at 'j' is
    // greater than the 'key', shift the element at 'j' one
    // position to the right.
    while j >= 0 and key < nums[j]:
      nums[j + 1] = nums[j]
      j = j - 1
    
    // Insert the 'key' into its correct position.
    nums[j + 1] = key
    
  // Return the sorted array.
  return nums


### Time Complexity
O(n^2)

### Space Complexity
O(1)
