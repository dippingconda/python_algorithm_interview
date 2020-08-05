"""
https://leetcode.com/problems/odd-even-linked-list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def odd_even(linked: Node) -> Node:
    if linked is None:
        return None

    odd = linked
    even = linked.next
    even_head = even

    #while even and even.next:          # these conditions are the same.
    while odd.next and odd.next.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = even_head
    return linked



if __name__ == '__main__':
    test_case = Node(1)
    test_case.next = Node(2)
    test_case.next.next = Node(3)
    test_case.next.next.next = Node(4)
    test_case.next.next.next.next = Node(5)
    test_case.next.next.next.next.next = Node('NULL')
    result = odd_even(test_case)
    while result:
        print(result.data)
        result = result.next
