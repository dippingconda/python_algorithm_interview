"""
https://leetcode.com/problems/sort-list
"""
from typing import List


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class SingleLinked:
    def __init__(self):
        self.head = None

    def insert(self, nums: List[int]):
        self.head = Node(nums.pop(0))
        self.node = self.head
        while nums:
            self.node.next = Node(nums.pop(0))
            self.node = self.node.next

        return self.head


def merge(nodes_1: Node, nodes_2: Node) -> Node:
    if nodes_1 and nodes_2:
        if nodes_1.val > nodes_2.val:
            nodes_1, nodes_2 = nodes_2, nodes_1
        nodes_1.next = merge(nodes_1.next, nodes_2)

    return nodes_1 or nodes_2


# solution 1
# you can learn how to handle linked list for divide and conquer
def merge_sort(head: Node) -> Node:
    if not (head and head.next):
        return head

    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    left = merge_sort(head)
    right = merge_sort(slow)

    return merge(left, right)


# solution 2
# this is way much faster than solution 1
def sort_list(head: Node) -> Node:
    nums = []
    node = head
    while node:
        nums.append(node.val)
        node = node.next

    nums.sort()

    node = head
    for val in nums:
        node.val = val
        node = node.next

    return head


if __name__ == '__main__':
    single_linked = SingleLinked()
    head = single_linked.insert([4, 2, 1, 3])
    print(f'{sort_list(head).val}')
    print(f'{merge_sort(head).val}')

