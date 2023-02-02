# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.
# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.
 
# Example 1:
 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

# Example 2:
 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

# Example 3:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
# Output: 0

from collections import defaultdict, deque

#Solution 1 - (參考網路)

# 解題邏輯: 

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        def kahnsalgo():
            N = len(hasApple)
		        # N => 樹產生蘋果的點
            E = len(edges)
		        # E => 有幾條線
            indegrees = [0] * N
		        # 每個頂點的值初始化為0
            
            for u,v in edges:
		        # 取出u點和v點
                indegrees[v] += 1
		            # 在頂點列表中，u點探訪過v點，因此+1值
                indegrees[u] += 1
                # 在頂點列表中，v點探訪過u點，因此+1值
            queue = deque()
	          # 雙端佇列 : deque 能夠同時操作佇列的兩端。

            for i,ind in enumerate(indegrees):
		        # 從頂點列表中取得索引值i(第幾個頂點)和其值
                if ind == 1 and not hasApple[i]: # if there's only 1 in-edge and there's no apple -> empty leaf
		            # 如果該頂點的值只有1，且沒有蘋果時
                    queue.append(i) # add for removal
		   		          # 在雙端佇列中增加其索引，之後方便移除
                    
            removed_nodes = 0
		        # 移除的點設為0
            while queue:
		        # 當佇列還有點時，進入迴圈
                node = queue.popleft()
                # node = 從佇列中取得最左邊的值賦與node，並且刪除佇列中的點

                if node == 0: # we cannot remove root in any case
			          # 若node為0則跳過，0是樹根
                    continue
                
                for nei in adj_list[node]:
		            # 從adj_list[node]中取得nei的值 (node有出現在幾個點中)
			          # 假設 node = 3, nei = 2, defaultdict(<type 'set'>, {0: set([1, 2]), 1: set([0, 4, 5]), 2: set([0, 3, 6]), 3: set([2]), 4: set([1]), 5: set([1]), 6: set([2])}))

                    adj_list[nei].discard(node)
		   		          # 從頂點nei中，移除node節點 (該點沒有蘋果且沒有其他連結)

                    indegrees[nei] -= 1 # remove edge from v,u
                    # 頂點nei要減去1的值，因為少了一條線

                    if indegrees[nei] == 1 and not hasApple[nei]: # another leaf? add to remove
                    # 若是nei減去1條線後，剩下一條線和沒有蘋果時

                        queue.append(nei)
                        # 雙向佇列則增加nei頂點

                    removed_nodes += 1 # count removed nodes
                    # 跑完以上的內容，刪除頂點的值+1

            return (E - removed_nodes) * 2 # (all edges - edges_to_empty_nodes) * 2
            # 最後return回去總共的線減去移除的節點後 * 2 => 雙向通道
        
        adj_list = defaultdict(set)
        for u,v in edges: adj_list[u].add(v), adj_list[v].add(u)
        return kahnsalgo()
 

 #Solution 2 - (參考網路)

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        visited = [False]*n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return self.dfs(0, graph, 0, hasApple, visited) * 2
        
    def dfs(self, node, graph, depth, hasApple, visited):
        visited[node] = True
        total = 0
        for child in graph[node]:
            if visited[child]:
                continue
            value = self.dfs(child, graph, depth + 1, hasApple, visited)
            if value > 0:
                total += value - depth
        if total == 0 and hasApple[node]:
            return depth
        elif total != 0:
            return total + depth
        else:
            return 0


#Solution 3 - (參考網路)

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = defaultdict(list)
        for src,des in edges:
            graph[src].append(des)
            graph[des].append(src)
        visited = set()
        def dfs(node):
            res = 0
            for edge in graph[node]:
                if edge not in visited:
                    visited.add(edge)
                    val, isApple = dfs(edge)
                    res += val+int(isApple)
            return res, res>0 or hasApple[node]
        visited.add(0)
        output= dfs(0)
        return output[0]*2
