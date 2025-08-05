class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
                if grid[i][j] == 1:
                    fresh += 1
        
        directions = [(-1,0), (1,0), (0,-1),(0,1)]  
        max_time = 0
        while q:
            x, y, level = q.popleft()

            for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny, level+1))
                        max_time = max(max_time, level+1)
                        fresh -=1
                        
                       
       
        return max_time if fresh == 0 else -1

        








        