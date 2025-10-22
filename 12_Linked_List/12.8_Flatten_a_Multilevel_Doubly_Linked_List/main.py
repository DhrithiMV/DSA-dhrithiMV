class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            curr = prev.next
            nxt = kth.next

            # Reverse group
            prev_sub, curr_sub = kth.next, curr
            for _ in range(k):
                temp = curr_sub.next
                curr_sub.next = prev_sub
                prev_sub = curr_sub
                curr_sub = temp

            temp = prev.next
            prev.next = kth
            prev = temp
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
    l = build_list([1,2,3,4,5])
    rev = sol.reverseKGroup(l, 3)
    print_list(rev)
