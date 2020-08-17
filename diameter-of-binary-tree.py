"""
https://leetcode.com/problems/diameter-of-binary-tree
"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def diameter_binary_tree(root: TreeNode) -> int:

    def dfs(node: TreeNode):
        global diameter
        if not node:
            return -1

        left_distance = dfs(node.left)
        right_distance = dfs(node.right)

        diameter = max(diameter, left_distance + 1 + right_distance + 1)
        return max(left_distance, right_distance) + 1

    dfs(root)
    return diameter


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    diameter = 0
    print(f'{diameter_binary_tree(tree)}')