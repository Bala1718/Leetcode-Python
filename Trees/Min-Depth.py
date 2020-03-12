class Solution:
    def min_Depth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.min_Depth(root.right)+1
        if not root.right:
            return self.min_Depth(root.left)+1
        
        m_left = self.min_Depth(root.left)
        m_right = self.min_Depth(root.right)
        m_depth = min(m_left,m_right) + 1
        return m_depth
