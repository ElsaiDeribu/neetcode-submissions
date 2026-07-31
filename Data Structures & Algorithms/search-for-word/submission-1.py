class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        curr = []

        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        
        def dfs(row, col):

            if len(curr) == len(word):
                return ''.join(curr) == word

            if len(curr) > len(word):
                return

            res = False
            for dr, dc in directions:
                R, C = dr + row, dc + col

                if (R,C) not in visited and inbound(R,C):
                    visited.add((R,C))
                    curr.append(board[R][C])
                    res = res or dfs(R, C)
                    curr.pop()
                    visited.remove((R,C))



            return res

        

        for row in range(len(board)):
            for col in range(len(board[0])):
                curr.append(board[row][col])
                visited.add((row, col))
                if dfs(row, col):
                    return True
                visited.remove((row, col))
                curr.pop()

        return False

















        
        