"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_tree(self, nums: List[str]) -> TreeNode:
        from collections import deque

        idx = 0
        self.root = TreeNode(int(nums[idx]))
        idx += 1
        queue = deque([self.root])

        while queue and idx < len(nums):
            node = queue.popleft()
            if node:
                if nums[idx] != 'null':
                    node.left = TreeNode(int(nums[idx]))
                    queue.append(node.left)
                idx += 1
                if nums[idx] != 'null':
                    node.right = TreeNode(int(nums[idx]))
                    queue.append(node.right)
                idx += 1

        return self.root


def min_diff_in_BST_dfs(root: TreeNode) -> int:
    global prev, result

    if root.left:
        min_diff_in_BST_dfs(root.left)

    result = min(result, root.val - prev)
    prev = root.val

    if root.right:
        min_diff_in_BST_dfs(root.right)

    return result


def min_diff_in_BST_loop(root: TreeNode) -> int:
    prev = -float('inf')
    result = float('inf')

    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()

        result = min(result, node.val - prev)
        prev = node.val

        node = node.right

    return result

if __name__ == '__main__':
    root = ['4', '2', '6', '1', '3', 'null', 'null']
    tree = BinarySearchTree()
    binary_search_tree = tree.build_tree(root)
    prev = -float('inf')
    result = float('inf')
    print(f'{min_diff_in_BST_dfs(binary_search_tree)}')
    print(f'{min_diff_in_BST_loop(binary_search_tree)}')

