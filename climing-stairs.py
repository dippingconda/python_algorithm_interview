"""
https://leetcode.com/problems/climing-stairs
"""

# 피보나치 수열과 동일한 방법으로 풀이
def climb_stairs(num_stairs: int) -> int:
    global dp

    if num_stairs in dp:
        return dp[num_stairs]

    dp[num_stairs] = dp[num_stairs - 1] + dp[num_stairs - 2]
    return dp[num_stairs]


if __name__ == '__main__':
    test_case = 3
    dp = {1: 1, 2: 2}
    print(f'{climb_stairs(test_case)}')