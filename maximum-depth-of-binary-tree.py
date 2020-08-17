"""
https://leetcode.com/problems/maximum-depth-of-binary-tree
"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def max_depth(root: TreeNode) -> int:
    from collections import deque
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    depth = 0

    # BFS
    while queue:
        depth += 1
        print(len(queue))
        for _ in range(len(queue)):         # len(queue) = 해당 level의 node 수
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    print(f'max depth = {max_depth(tree)}')
