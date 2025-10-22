class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeLoop(self, head):
        slow = fast = head
        loop_found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop_found = True
                break
        if not loop_found:
            return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        while fast.next != slow:
            fast = fast.next
        fast.next = None

    def printList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = head.next  # create loop
    sol = Solution()
    sol.removeLoop(head)
    sol.printList(head)
