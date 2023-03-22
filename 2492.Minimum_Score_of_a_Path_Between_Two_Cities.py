# 2492. Minimum Score of a Path Between Two Cities

# You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.
# The score of a path between two cities is defined as the minimum distance of a road in this path.
# Return the minimum possible score of a path between cities 1 and n.
# Note:
# •	A path is a sequence of roads between two cities.
# •	It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
# •	The test cases are generated such that there is at least one path between 1 and n.
 
# Example 1:
 
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.

# Example 2:
 
# Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
# Output: 2
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

import sys
from collections import deque
from typing import List, Tuple
from math import inf

#Solution 1 : (參考網路)

# 解題邏輯 : 
# 使用BFS搜尋，建立ADJ LIST(每個點拜訪過的其他點與距離)

class Solution:
    def bfs(self, n: int, adj: List[List[Tuple[int, int]]]) -> int:
        visited = [False] * (n+1)
        q = deque()
        answer = inf

        q.append(1)
        visited[1] = True

        while q:
            node = q.popleft()

            for edge in adj[node]:
                answer = min(answer, edge[1])
                if not visited[edge[0]]:
                    visited[edge[0]] = True
                    q.append(edge[0])
        return answer
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))
        return self.bfs(n, adj)
 

#Solution 2 (參考網路)

# 解題邏輯 : 
# 使用DFS搜尋，依序拜訪每個城市。

class Solution:
    def __init__(self):
        self.answer = sys.maxsize

    def dfs(self, node, adj, visit):
        visit[node] = True
        if node not in adj:
            return
        for edge in adj[node]:
            self.answer = min(self.answer, edge[1])
            if not visit[edge[0]]:
                self.dfs(edge[0], adj, visit)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = {}
        for road in roads:
            adj.setdefault(road[0], []).append([road[1], road[2]])
            adj.setdefault(road[1], []).append([road[0], road[2]])

        visit = [False] * (n + 1)
        self.dfs(1, adj, visit)

        return self.answer
 
