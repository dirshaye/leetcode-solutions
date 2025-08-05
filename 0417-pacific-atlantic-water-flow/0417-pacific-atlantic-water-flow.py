class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if ( 0 <= r < rows and 0 <= c < cols and (r,c) not in visited and heights[r][c] >= prev_height):
                visited.add((r,c)) 
                directions = [(-1,0),(1,0), (0,-1), (0, 1)]
                for dx, dy in directions:
                    nx, ny = dx+r, dy + c
                    dfs(nx, ny, visited, heights[r][c])

                
            
          

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result


        
            

            




        