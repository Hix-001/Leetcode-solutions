# 06/10/2026
# Easy
# LeetCode 94: Binary Tree Inorder Traversal using an iterative stack.
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stack = []
        curr = root        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left                
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right            
        return res
if __name__ == "__main__":
    sol = Solution()    
    # Example 1: root = [1,null,2,3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print(sol.inorderTraversal(root1))    
    # Example 3: root = []
    print(sol.inorderTraversal(None))    
    # Example 4: root = [1]
    print(sol.inorderTraversal(TreeNode(1)))