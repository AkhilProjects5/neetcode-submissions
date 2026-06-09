class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        max_area = 0

        def continuity(rows,cols,row,col,visited):
            if row < 0 or row >= rows or col<0 or col >= cols or grid[row][col] == 0 or visited[row][col] == 1 :
                return 0
            visited[row][col] = 1
            return(1+ 
            (continuity(rows,cols,row+1,col,visited)
            +continuity(rows,cols,row-1,col,visited)
            +continuity(rows,cols,row,col+1,visited)
            +continuity(rows,cols,row,col-1,visited)))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and visited[row][col] == 0:
                    max_area = max(max_area,continuity(rows,cols,row,col,visited))
        
        return max_area
           




        