# 22/09/2026
# Medium
# LeetCode 143: Reorder List using fast/slow pointers and in-place reversal.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)
if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol = Solution()
    sol.reorderList(head1)
    print_list(head1)
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol.reorderList(head2)
    print_list(head2)
    