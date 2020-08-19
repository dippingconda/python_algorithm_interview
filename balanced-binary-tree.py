"""
https://leetcode.com/problems/balanced-binary-tree
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


class binaryTree:
    def __init__(self):
        self.root = None
        self.cur_node = self.root

    def insert(self, data):
        from collections import deque
        queue = deque()
        idx = 0
        self.root = TreeNode(int(data[idx]))
        queue.append(self.root)
        idx += 1
        while queue and idx < len(data):
            node = queue.popleft()
            if node:
                if data[idx] != 'null':
                    node.left = TreeNode(int(data[idx]))
                    queue.append(node.left)
                idx += 1
                if data[idx] != 'null':
                    node.right = TreeNode(int(data[idx]))
                    queue.append(node.right)
                idx += 1

        return self.root


def is_balanced(root: TreeNode) -> bool:

    def dfs(node: TreeNode):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if abs(left - right) > 1 or \
                left == -1 or right == -1:
            return -1

        return max(left, right) + 1

    return dfs(root) != -1

if __name__ == '__main__':
    test_case = ['3', '9', '20', 'null', 'null', '15', '7']
    tree = binaryTree().insert(test_case)
    print(f'{is_balanced(tree)}')
    test_case = ['1', '2', '2', '3', '3', 'null', 'null', '4', '4']
    tree = binaryTree().insert(test_case)
    print(f'{is_balanced(tree)}')
