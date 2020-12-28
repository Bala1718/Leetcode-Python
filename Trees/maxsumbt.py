class solution(object):
    def maxpathSum(self,root):
        self.globalmax = float('-inf')
        self.submaxpathsum(root)
        return self.globalmax
    def submaxpathSum(self,root):
        if not root:
            return 0
        left = max(0, self.submaxpathsum(root.left))
        right = max(0, self.submaxpathsum(root.right))

        self.globalmax = max(self.globalmax, left + root.val + right)
        return max(left + root.val, right + root.val)