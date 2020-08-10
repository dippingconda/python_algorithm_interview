"""
https://leetcode.com/problems/valid-parentheses
"""


def valid_parentheses(parentheses: str) -> bool:
    look_up = {')': '(',
               ']': '[',
               '}': '{'}

    stack = []
    for s in parentheses:
        if s not in look_up:
            stack.append(s)
        # 모두 닫는 괄호인 경우라서 스택이 비었거나, 스택과 look up이 불일치 할 경우
        elif not stack or stack.pop() != look_up[s]:
            return False

    return len(stack) == 0




if __name__ == '__main__':
    input_parentheses = '()[]{}'
    print(f'{valid_parentheses(input_parentheses)}')
    input_parentheses = ')]}'
    print(f'{valid_parentheses(input_parentheses)}')
    input_parentheses = '()[]{'
    print(f'{valid_parentheses(input_parentheses)}')
    input_parentheses = '(}[]{}'
    print(f'{valid_parentheses(input_parentheses)}')
