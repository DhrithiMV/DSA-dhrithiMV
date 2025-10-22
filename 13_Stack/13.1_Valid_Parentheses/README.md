# Valid Parentheses
**Topic:** Stack

**Type:** In-Session

Problem :

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.

An input string is **valid** if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.



Constraints

1 ≤ s.length ≤ 10^4
s consists of parentheses only.


Input Format

* A single string `s` consisting only of the characters `'(){}[]'`.

Output Format

Return `True` if the string is valid, otherwise return `False`.


Examples

| **Input**  | **Output** | **Explanation**                               |
| ---------- | ---------- | --------------------------------------------- |
| `"()"`     | `True`     | `'('` matches `')'` in correct order          |
| `"()[]{}"` | `True`     | All brackets match properly                   |
| `"(]"`     | `False`    | `'('` does not match `']'`                    |
| `"([)]"`   | `False`    | `'['` and `')'` are mismatched within nesting |
| `"{[]}"`   | `True`     | Both `'['` and `'{'` are closed correctly     |
| `")("`     | `False`    | Cannot have closing bracket before opening    |
| `"((("`    | `False`    | Three opening brackets and no closing ones    |



### Approach
Describe your approach here...

### Pseudocode

push(x):
    Append x to queue
pop():
    Rotate queue until last element, then pop and return it
top():
    Rotate until last element, but return and keep it
empty():
    Return if queue is empty

### Time Complexity

push: O(1)  
pop/top: O(n)  

### Space Complexity

O(n)

