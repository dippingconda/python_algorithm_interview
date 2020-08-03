"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""
from typing import List


def buy_and_sell(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == '__main__':
    input_price = [7, 1, 5, 3, 6, 4]
    print(f'{buy_and_sell(input_price)}')