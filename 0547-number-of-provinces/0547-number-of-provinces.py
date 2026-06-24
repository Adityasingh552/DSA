class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[]for i in range(n)]
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in range (n):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    dfs(nei)
        count = 0

        for i in range (n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count