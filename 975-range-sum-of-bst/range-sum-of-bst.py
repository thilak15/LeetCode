# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_range=0
        if not root:
            return 0
        if low<=root.val<=high:
            sum_range+=root.val
        if root.val>low:
            sum_range+=self.rangeSumBST(root.left,low,high)
        if root.val<high:
            sum_range+=self.rangeSumBST(root.right,low,high)
        return sum_range


        