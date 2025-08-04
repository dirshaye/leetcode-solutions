class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
     

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1

            while q:
                x, y = q.popleft()
                for a, b in [(-1,0), (1,0), (0,-1),(0,1)]:
                    nx, ny = x+a, y+b
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        q.append((nx,ny))
                        area +=1
            return area 

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area= max(max_area, bfs(i,j))

        return max_area




        