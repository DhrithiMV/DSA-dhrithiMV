# Reverse a Linked List
# Topic: Linked List
# Type: In-Session

from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Helper to build and print list for demo
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

if __name__ == "__main__":
    sol = Solution()
    l = build_list([1,2,3,4,5])
    rev = sol.reverseList(l)
    print_list(rev)
