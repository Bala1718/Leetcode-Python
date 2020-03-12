class Solution:
    def minDepth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1
        
        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)
        min_depth = min(min_left,min_right) + 1
        return min_depth
