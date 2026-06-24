class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph  = [[]for _ in range (n + 1)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n


        def dfs(node):
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        dfs(source)
        return visited[destination]