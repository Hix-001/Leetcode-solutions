# 03/10/2026
# Medium
# LeetCode 701: Insert into a Binary Search Tree using O(1) space iterative traversal.

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)            
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left                
        return root