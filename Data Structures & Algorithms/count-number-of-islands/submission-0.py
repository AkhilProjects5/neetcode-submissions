class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        island = 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def continuity(grid,rows,cols,a,b,visited):
            if (a<0 or a>=rows) or (b<0 or b>=cols) or visited[a][b] == 1 or grid[a][b] == "0":
                return

            visited[a][b] = 1
            continuity(grid,rows,cols,a+1,b,visited)
            continuity(grid,rows,cols,a,b+1,visited)
            continuity(grid,rows,cols,a-1,b,visited)
            continuity(grid,rows,cols,a,b-1,visited)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    continuity(grid,rows,cols,row,col,visited)
                    island += 1

        return island
        