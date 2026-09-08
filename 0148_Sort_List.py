# 08/09/2026
# Medium
# LeetCode 148: Sort List using Top-Down Merge Sort.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
            
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        dummy = ListNode(0)
        curr = dummy
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
            
        if left:
            curr.next = left
        if right:
            curr.next = right
            
        return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("[" + ", ".join(res) + "]")

if __name__ == "__main__":
    node4 = ListNode(4)
    node2 = ListNode(2)
    node1 = ListNode(1)
    node3 = ListNode(3)
    node4.next = node2
    node2.next = node1
    node1.next = node3
    
    sol = Solution()
    sorted_head = sol.sortList(node4)
    print_list(sorted_head)