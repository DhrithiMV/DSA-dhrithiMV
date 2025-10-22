import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        dummy = ListNode()
        curr = dummy
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
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
    l1 = build_list([1,4,5])
    l2 = build_list([1,3,4])
    l3 = build_list([2,6])
    merged = sol.mergeKLists([l1, l2, l3])
    print_list(merged)
