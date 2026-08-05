class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:    

        # TC: O(m * n)
        # SC: O(m * n)

        ans = 0
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])


        def check(row, col):

            grid[row][col] = 0
            res = 1
            
            for dr, dc in dirs:
                new_row = dr + row
                new_col = dc + col
                if is_inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    res += check(new_row, new_col)
                    
            return res


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    ans = max(ans, check(row, col))



        return ans
        