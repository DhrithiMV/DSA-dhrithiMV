class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

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
    l1 = build_list([1,3,5])
    l2 = build_list([2,4,6])
    merged = sol.mergeTwoLists(l1, l2)
    print_list(merged)
