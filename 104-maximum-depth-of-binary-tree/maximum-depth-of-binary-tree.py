# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """q=deque()
        level=0
        if root:
            q.append(root)
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level"""
        # Time complexity O(n)
        # Space Complexity O(n)
        # We can do this by usng recursion which leads to the auxilary space complexity of O(n)
        if not root :
            return 0
        lh=self.maxDepth(root.left)
        rh=self.maxDepth(root.right)

        height=1+max(lh,rh)

        return height

