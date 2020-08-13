"""
https://leetcode.com/problems/combination-sum
"""
from typing import List


def comb_sum(candidates: List[int], target: int) -> List[int]:
    result = []

    def dfs(sub: int, start: int, path: List[int]):
        if sub < 0:
            return
        if sub == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if sub - candidates[i] < 0:
                continue
            dfs(sub - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


if __name__ == '__main__':
    test_case = {'candidates': [2, 3, 6, 7], 'target': 7}
    print(f"{comb_sum(test_case['candidates'], test_case['target'])}")