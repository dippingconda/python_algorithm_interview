"""
https://leetcode.com/problems/merge-two-sorted-list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(list_1: Node, list_2: Node) -> Node:
    if (not list_1) or (list_2 and list_1.data > list_2.data):
        list_1, list_2 = list_2, list_1

    if list_1:
        list_1.next = merge(list_1.next, list_2)

    return list_1


if __name__ == '__main__':
    input_1 = Node(1)
    input_1.next = Node(2)
    input_1.next.next = Node(4)
    input_2 = Node(1)
    input_2.next = Node(3)
    input_2.next.next = Node(4)
    result = merge(input_1, input_2)
    while result:
        print(result.data)
        result = result.next
