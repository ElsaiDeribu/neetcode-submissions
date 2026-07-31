class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sects = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                
                num = board[row][col]
                if num == ".":
                    continue

                sec = (row // 3, col // 3)

                if (num in rows[row]) or (num in cols[col]) or (num in sects[sec]):
                    return False

                rows[row].add(num)
                cols[col].add(num)
                sects[sec].add(num)

        return True
                
        