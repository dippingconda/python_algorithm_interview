"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not inorder:
        return None

    idx = inorder.index(preorder.pop(0))

    node = TreeNode(inorder[idx])
    node.left = build_tree(preorder, inorder[:idx])
    node.right = build_tree(preorder, inorder[idx+1:])

    return node


if __name__ == '__main__':
    tc_preorder = [3, 9, 20, 15, 7]
    tc_inorder = [9, 3, 15, 20, 7]
    binary_tree = build_tree(tc_preorder, tc_inorder)
    print(f'{binary_tree.val}')
