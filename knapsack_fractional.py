from typing import List, Tuple


def fractional_knapsack(items: List[Tuple[int]]) -> float:
    capacity = 15
    pack = []

    for cost, weight in items:
        pack.append((cost / weight, cost, weight))
    pack.sort(reverse=True)

    total_value: float = 0
    for _, cost, weight in pack:
        if capacity - weight >= 0:
            capacity -= weight
            total_value += cost
        else:
            fraction = capacity / weight
            total_value += cost * fraction
            break

    return total_value


if __name__ == '__main__':
    cargo = [(4, 12),
             (2, 1),
             (10, 4),
             (1, 1),
             (2, 2)]
    print(f'{fractional_knapsack(cargo)}')