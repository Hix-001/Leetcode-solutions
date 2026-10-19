# 07/08/2026
# Medium
# LeetCode 24: Swap Nodes in Pairs using a dummy node and pointer manipulation.

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
            
        return dummy.next