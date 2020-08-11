"""
https://leetcode.com/problems/number-of-islands
"""
from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    count = 0
    visited = []
    dx = [1, -1]
    dy = [1, -1]

    def dfs(i: int, j: int):
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return
        if (i, j) not in visited:
            visited.append((i, j))
            dfs(i + dy[0], j)
            dfs(i + dy[1], j)
            dfs(i, j + dx[1])
            dfs(i, j + dx[0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '0' and (i, j) not in visited:
                dfs(i, j)
                count += 1

    return count


def solution(grid: List[List[str]]) -> int:
    count = 0

    def dfs(i: int, j: int):
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
             grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


if __name__ == '__main__':
    test_case = [['1', '1', '1', '1', '0'],
                 ['1', '1', '0', '1', '0'],
                 ['1', '1', '0', '0', '0'],
                 ['0', '0', '0', '0', '0']]
    print(f'{number_of_islands(test_case)}')
    print(f'{solution(test_case)}')

    test_case = [['1', '1', '0', '0', '0'],
                 ['1', '1', '0', '0', '0'],
                 ['0', '0', '1', '0', '0'],
                 ['0', '0', '0', '1', '1']]
    print(f'{number_of_islands(test_case)}')
    print(f'{solution(test_case)}')
