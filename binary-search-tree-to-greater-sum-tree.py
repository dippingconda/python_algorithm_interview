"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val: int = data
        self.left = self.right = None


def build_tree(nums: List[int]):
    from collections import deque
    root = TreeNode(int(nums[0]))
    idx: int = 1
    queue = deque()
    queue.append(root)

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

    return root


def BST_to_GST(root: TreeNode) -> TreeNode:
    global sum

    if root:
        BST_to_GST(root.right)
        sum += root.val
        root.val = sum
        BST_to_GST(root.left)

    return root


if __name__ == '__main__':
    test_case = ['4', '1', '6', '0', '2', '5', '7', 'null', 'null', 'null', '3', 'null', 'null', 'null', '8']
    sum: int = 0
    bst = build_tree(test_case)
    gst = BST_to_GST(bst)
    print(f'{gst.val}')