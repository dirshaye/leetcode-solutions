class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        if not grid:
            return 0

        rows,cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
         
            queue = deque()
            queue.append((r,c))
            grid[r][c] = "0"

            while queue:
                x, y = queue.popleft()
                for a, b in [(-1,0), (1,0), (0,-1), (0, 1)]:
                    nx, ny = x+a, y+b
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx,ny))
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i,j)
                    islands +=1
        
        return islands

        