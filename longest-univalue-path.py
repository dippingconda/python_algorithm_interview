"""
https://leetcode.com/problems/longest-univalue-path
"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


def longest_univalue_path(root: TreeNode) -> int:

    def dfs(node: TreeNode) -> int:
        global path_count

        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if node.left and node.val == node.left.val:
            left += 1
        else:
            left = 0
        if node.right and node.val == node.right.val:
            right += 1
        else:
            right = 0

        path_count = max(path_count, left + right)

        return max(left, right)
    dfs(root)
    return path_count


if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(1)
    tree.right.right = TreeNode(5)
    path_count = 0
    print(f'{longest_univalue_path(tree)}')
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(5)
    path_count = 0
    print(f'{longest_univalue_path(tree)}')
    tree = TreeNode(4)
    tree.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(5)
    tree.left.left.left = TreeNode(4)
    tree.left.left.right = TreeNode(4)
    path_count = 0
    print(f'{longest_univalue_path(tree)}')
    tree = TreeNode(4)
    tree.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(5)
    tree.left.left.left = TreeNode(4)
    tree.left.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(4)
    tree.left.right.right = TreeNode(4)
    path_count = 0
    print(f'{longest_univalue_path(tree)}')
