"""
https://leetcode.com/reverse-linked-list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(linked: Node) -> Node:
    def reversing(cur: Node, prev: Node = None):
        if not cur:
            return prev
        next, cur.next = cur.next, prev
        return reversing(next, cur)

    return reversing(linked)


if __name__ == '__main__':
    input_list = Node(1)
    input_list.next = Node(2)
    input_list.next.next = Node(3)
    input_list.next.next.next = Node(4)
    input_list.next.next.next.next = Node(5)
    result = reverse(input_list)
    while result:
        print(result.data)
        result = result.next
