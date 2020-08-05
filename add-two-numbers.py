"""
https://leetcode.com/problems/add-two-numbers
"""
from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_two_numbers(op_1: Node, op_2: Node) -> List:
    num_1 = op_1
    num_2 = op_2
    result = []
    carry = 0
    while num_1 or num_2:
        remainder, quotient = divmod(num_1.data + num_2.data, 10)
        result.append(quotient + carry)
        carry = remainder
        num_1 = num_1.next
        num_2 = num_2.next
    while num_1:
        if carry != 0:
            result.append(num_1.data + carry)
        else:
            result.append(num_1.data)
        num_1 = num_1.next
    while num_2:
        if carry != 0:
            result.append(num_2.data + carry)
        else:
            result.append(num_2.data)
        num_2 = num_2.next

    return result

def add_two_numbers_solution(linked_1:Node, linked_2: Node) -> Node:
    root = cur = Node(0)
    carry = 0

    while linked_1 or linked_2 or carry:
        sum = 0
        if linked_1:
            sum += linked_1.data
            linked_1 = linked_1.next
        if linked_2:
            sum += linked_2.data
            linked_2 = linked_2.next

        carry, val = divmod(sum + carry, 10)
        cur.next = Node(val)
        cur = cur.next

    return root.next




if __name__ == '__main__':
    operand_1 = Node(2)
    operand_1.next = Node(4)
    operand_1.next.next = Node(3)
    operand_2 = Node(5)
    operand_2.next = Node(6)
    operand_2.next.next = Node(4)
    print(' -> '.join(map(str, add_two_numbers(operand_1, operand_2))))
    result = add_two_numbers_solution(operand_1, operand_2)
    while result:
        print(f'{result.data}')
        result = result.next
