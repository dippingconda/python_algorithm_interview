"""
https://leetcode.com/problems/range-sum-of-bst
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, nums: List[str]):
        from collections import deque

        idx = 0
        self.root = TreeNode(int(nums[idx]))
        queue = deque([self.root])
        idx += 1
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


def range_sum_BST_dfs(root: TreeNode, L: int, R: int) -> int:

    def dfs(node: TreeNode):
        if not node:
            return 0

        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)

        return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)


def range_sum_BST_loop(root: TreeNode, L: int, R: int) -> int:

    stack = [root]
    range_sum = 0
    while stack:
        node = stack.pop()
        if not node:
            continue

        if node.val < L:
            stack.append(node.right)
        elif node.val > R:
            stack.append(node.left)

        if L <= node.val <= R:
            range_sum += node.val
            stack.extend([node.left, node.right])

    return range_sum


if __name__ == '__main__':
    root = ['10', '5', '15', '3', '7', 'null', '18']
    L = 7
    R = 15
    tree = BinarySearchTree()
    binary_search_tree = tree.insert_node(root)
    print(f'{range_sum_BST_dfs(binary_search_tree, L, R)}')
    print(f'{range_sum_BST_loop(binary_search_tree, L, R)}')
