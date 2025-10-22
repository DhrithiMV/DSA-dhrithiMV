# Largest Rectangle in Histogram
**Topic:** Stack

**Type:** Home Challenge


Problem :

Given an array of integers `heights` representing the histogram's bar heights (where the width of each bar is `1`), return the **area of the largest rectangle** that can be formed within the histogram.



### **Constraints**


1 ≤ heights.length ≤ 10^5
0 ≤ heights[i] ≤ 10^4



### **Input Format**

* A list of integers `heights`, where each element represents the height of a bar in the histogram.

### **Output Format**

* Return a single integer — the maximum rectangular area that can be formed.



### Examples

| **Input**               | **Output** | **Explanation**                                                                  |
| ----------------------- | ---------- | -------------------------------------------------------------------------------- |
| `[2, 1, 5, 6, 2, 3]`    | `10`       | Rectangle covering bars 5 and 6 (height = 5, width = 2) gives area `5 × 2 = 10`. |
| `[2, 4]`                | `4`        | Use tallest bar (4) or both bars: `min(2, 4) × 2 = 4`.                           |
| `[6, 2, 5, 4, 5, 1, 6]` | `12`       | Bars 3–5 (heights 5, 4, 5): height = 4, width = 3, area = `4 × 3 = 12`.          |
| `[1, 1, 1, 1]`          | `4`        | All bars same height: height = 1, width = 4, area = `4`.                         |
| `[4, 3, 2, 1]`          | `6`        | Bars 1–3 (heights 4, 3, 2): min height = 2, width = 3, area = `6`.               |
| `[0, 0, 0]`             | `0`        | All bars have zero height.                                                       |
| `[2, 1, 2]`             | `3`        | Max rectangle formed by all three bars: height = 1, width = 3, area = `3`.       |


### Approach
Describe your approach here...

### Pseudocode

push(x):
    Add x to main stack
    If min_stack is empty or x <= min_stack top, push x to min_stack

pop():
    Remove top from main stack
    If popped == min_stack top, pop min_stack

top():
    Return top of main stack

getMin():
    Return top of min_stack

### Time Complexity

O(1) for all operations

### Space Complexity

O(n)

