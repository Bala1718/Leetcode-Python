class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)

        def dfs(node, X, Y):
            d[X].append([Y, node.val])
            if node.left:
                dfs(node.left, X - 1, Y + 1)
            if node.right:
                dfs(node.right, X + 1, Y + 1)

        dfs(root, 0, 0)

        return [[val for Y, val in sorted(d[X])] for X in sorted(d)]