"""
https://leetcode.com/problems/invert-binary-tree
"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


def invert_tree(root: TreeNode) -> TreeNode:
    from collections import deque

    queue = deque()
    queue.append(root)
    head = root

    while queue:
        node = queue.popleft()
        if node is not None:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

    return head


if __name__ == '__main__':
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    result = invert_tree(tree)

    def dfs(node: TreeNode):
        if not node:
            return
        # 전위 순회
        print(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(result)

