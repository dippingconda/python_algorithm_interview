"""
https://leetcode.com/problems/swap-nodes-in-pairs
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_pair(linked: Node) -> Node:
    root = prev = Node(0)
    cur = linked
    while cur and cur.next:
        next = cur.next
        prev.next = next
        cur.next = next.next
        next.next = cur

        cur = cur.next
        prev = prev.next.next

    return root.next



if __name__ == '__main__':
    test_case = Node(1)
    test_case.next = Node(2)
    test_case.next.next = Node(3)
    test_case.next.next.next = Node(4)
    result = swap_pair(test_case)
    while result:
        print(result.data)
        result = result.next
