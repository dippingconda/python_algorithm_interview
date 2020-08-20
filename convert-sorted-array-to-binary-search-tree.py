"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


def sorted_array_to_BST(nums: List[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sorted_array_to_BST(nums[:mid])
    node.right = sorted_array_to_BST(nums[mid+1:])

    return node


if __name__ == '__main__':
    test_case = [-10, -3, 0, 5, 9]
    print(f'root node : {sorted_array_to_BST(test_case).val}')