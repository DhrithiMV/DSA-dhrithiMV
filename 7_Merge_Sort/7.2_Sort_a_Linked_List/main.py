# Sort a Linked List
# Topic: Merge Sort
# Type: Home Challenge
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    def findMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
# Demo
if __name__ == '__main__':
    # Helper function to convert list to linked list
    def list_to_linked(lst):
        dummy = ListNode(0)
        cur = dummy
        for val in lst:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
    
    # Helper function to convert linked list to list
    def linked_to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    
    sol = Solution()
    head = list_to_linked([4,2,1,3])
    sorted_head = sol.sortList(head)
    print(linked_to_list(sorted_head))
