"""
https://leetcode.com/problems/palindrome-linked-list
"""
"""
reversed_linked_list인 rev와 slow 를 이용하여 
palindrome 여부를 판단.
two-pointer 기법과 비슷 (역방향으로 순회하는 rev와 순방향으로 순회하는 slow를 비교)
"""


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def isPalindrome(single_linked_list: Node) -> bool:
    rev = None
    slow = fast = single_linked_list
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    """
    list 길이가 홀수인 경우,
    list의 중앙에 위치한 값은 palindrome 판별이 필요치 않은 값이므로 건너 뛰도록 한다.
    """
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


if __name__ == '__main__':
    input_1 = Node(1)
    input_1.next = Node(2)
    input_2 = Node(1)
    input_2.next = Node(2)
    input_2.next = Node(2)
    input_2.next = Node(1)
    print(f'{isPalindrome(input_1)}')
    print(f'{isPalindrome(input_2)}')
