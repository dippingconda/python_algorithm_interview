"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""
from typing import List


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None


def deserialize(arr: List[int]) -> TreeNode:
    from collections import deque
    if not arr:
        return None
    idx = 1
    root = TreeNode(arr[idx])
    queue = deque()
    queue.append(root)
    idx += 1

    while queue and idx < len(arr):
        node = queue.popleft()
        if arr[idx] is not None:
            node.left = TreeNode(arr[idx])
            queue.append(node.left)
        idx += 1
        if arr[idx] is not None:
            node.right = TreeNode(arr[idx])
            queue.append(node.right)
        idx += 1

    return root


def serialize(root: TreeNode) -> List[int]:
    from collections import deque

    result = [None]

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    return result


if __name__ == '__main__':
    test_case = [None, 1, 2, 3, None, None, 4, 5]
    tree = deserialize(test_case)
    tree_arr = serialize(tree)
    print(tree_arr)
