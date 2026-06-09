class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        def dfs(node,par):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
                
            return False

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

            visit = [False]*(n+1)

            if dfs(n1,-1):
                return [n1,n2]
        return []
            
        