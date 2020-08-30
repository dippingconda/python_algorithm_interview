"""
https://leetcode.com/problems/different-ways-to-add-parentheses
"""
from typing import List


def diff_ways_to_compute(expr: str) -> List[int]:

    def compute(left: List[int], right: List[int], op: str) -> List[int]:
        results = []

        for l_item in left:
            for r_item in right:
                results.append(eval(str(l_item) + op + str(r_item)))

        return results

    if expr.isdigit():
        return [int(expr)]

    answers = []
    for idx, val in enumerate(expr):
        if val in '+-*%':
            left_expr = diff_ways_to_compute(expr[:idx])
            right_expr = diff_ways_to_compute(expr[idx + 1:])

            answers.extend(compute(left_expr, right_expr, val))

    return answers


if __name__ == '__main__':
    test_case = '2-1-1'
    print(f'{diff_ways_to_compute(test_case)}')
    test_case = '2*3-4*5'
    print(f'{diff_ways_to_compute(test_case)}')
