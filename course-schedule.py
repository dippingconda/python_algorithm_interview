"""
https://leetcode.com/problems/course-schedule
"""
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {}
    for u, v in prerequisites:
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)

    visited = set()
    traced = set()

    def dfs(i):
        """
        * visited와 traced 차이
        ** traced는 graph 구조를 따라 아직 depth first로 탐색 중인 node들이 담겨있음
        ** visited는 이미 모든 탐색이 끝난 node들이 담겨 있음
        * 결론
        ** 현재 탐색 중인 node가 traced에 담겨있다는 것은
           현재 node를 포함하는 path가 탐색 중임을 의미함.
        ** 아직 탐색 중인 path에서 현재 node를 재방문 했다는 것은
           현재 node의 어떤 자식 노드가 현재 node를 가리키는 cycle이 발생했음을 의미함
        ** visited에 포함된 node들은 이미 cycle을 발생시키지 않는 것으로 판명된, 탐색이 끝난 노드들 이므로 재탐색을 진행하지 않음
        """
        if i in traced:
            return False

        if i in visited:
            return True

        traced.add(i)
        if i in graph:
            for node in graph[i]:
                if not dfs(node):
                    return False
        traced.remove(i)
        visited.add(i)
        return True

    for u in list(graph):
        if not dfs(u):
            return False
    return True




if __name__ == '__main__':
    #test_case = {'n': 2, 'course': [[1, 0]]}
    #print(f'{can_finish(test_case["n"], test_case["course"])}')
    #test_case = {'n': 2, 'course': [[1, 0], [0, 1]]}
    #print(f'{can_finish(test_case["n"], test_case["course"])}')
    #test_case = {'n': 3, 'course': [[0, 1], [0, 2], [1, 2]]}
    #print(f'{can_finish(test_case["n"], test_case["course"])}')
    test_case = {'n': 3, 'course': [[0, 1], [0, 2], [2, 0]]}
    print(f'{can_finish(test_case["n"], test_case["course"])}')
