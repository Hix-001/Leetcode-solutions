#22/07/2026
#Easy
# LeetCode 83: Remove Duplicates from Sorted List using a single pointer to bypass duplicate nodes.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head