class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        visited = set()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        def is_inbound(row, col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])

        
        def dfs(row, col):
            
            visited.add((row, col))

            for dr, dc in dirs:
                new_row = dr + row
                new_col = dc + col

                if is_inbound(new_row, new_col) and (new_row, new_col) not in visited and heights[new_row][new_col] >=  heights[row][col]:
                    dfs(new_row, new_col)


        for row in range(len(heights)):
            col = len(heights[0]) - 1
            if (row, col) not in visited:
                dfs(row, col)

        for col in range(len(heights[0])):
            row = len(heights) - 1
            if (row, col) not in visited:
                dfs(row, col)


        atlantic = visited.copy()

        visited = set()

        for col in range(len(heights[0])):
            row = 0
            if (row, col) not in visited:
                dfs(row, col)

        for row in range(len(heights)):
            col = 0
            if (row, col) not in visited:
                dfs(row, col)

        
        return [ [row,col] for row, col in visited if (row, col)  in atlantic]
