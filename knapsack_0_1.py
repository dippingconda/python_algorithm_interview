from typing import List, Tuple


def zero_one_knapsack(items: List[Tuple[int]]) -> float:
    capacity = 15
    pack = []

    for i in range(len(items) + 1):
        pack.append([])
        for capa in range(capacity + 1):
            if i == 0 or capa == 0:
                pack[i].append(0)
            elif items[i - 1][1] <= capa:
                pack[i].append(
                    max(
                        items[i-1][0] + pack[i-1][capa - items[i -1 ][1]],
                        pack[i - 1][capa]
                    )
                )
            else:
                pack[i].append(pack[i - 1][capa])

    return pack[-1][-1]



if __name__ == '__main__':
    cargo = [(4, 12),
             (2, 1),
             (10, 4),
             (1, 1),
             (2, 2)]
    print(f'{zero_one_knapsack(cargo)}')