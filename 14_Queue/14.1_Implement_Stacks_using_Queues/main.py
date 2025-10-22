class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return result

# Demo usage
if __name__ == "__main__":
    # Create a binary tree:   1
    #                         / \
    #                        2   3
    #                       / \
    #                      4   5
    node = TreeNode(1)
    node.left = TreeNode(2, TreeNode(4), TreeNode(5))
    node.right = TreeNode(3)
    sol = Solution()
    print(sol.preorderTraversal(node))  # Output: [1,2,4,5,3]
