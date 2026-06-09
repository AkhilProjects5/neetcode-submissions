class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        time = 0
        count_fresh = 0
        queue = collections.deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        for row in range(ROWS):
            for col in range(COLS) :
                if grid[row][col] == 1:
                    count_fresh +=1
                if grid[row][col] == 2:
                    queue.append((row,col))
        
        while count_fresh>0 and queue :
            length = len(queue)

            for i in range(length):
                r,c = queue.popleft()

                for dr , dc in directions:
                    row , col = r + dr , c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        grid[row][col] = 2 
                        queue.append((row,col))
                        count_fresh -=1

            time +=1

        return time if count_fresh == 0 else -1
        