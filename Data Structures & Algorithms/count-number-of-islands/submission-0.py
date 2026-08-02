class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def check(row, col):

            for dr, dc in dirs:
                new_row = dr + row
                new_col = dc + col

                if is_inbound(new_row, new_col) and grid[new_row][new_col] == "1": 
                    grid[new_row][new_col] = "0"
                    check(new_row, new_col)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count  += 1
                    check(row, col)


        return count



