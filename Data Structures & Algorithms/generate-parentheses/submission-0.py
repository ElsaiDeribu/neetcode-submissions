class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        pile = []


        def dfs(open, closed):

            if open == closed == n:
                ans.append(''.join(pile))
                return
            # open
            if open < n:
                pile.append("(")
                dfs(open + 1, closed)
                pile.pop()

            # close
            if open > closed:
                pile.append(")")
                dfs(open, closed + 1)
                pile.pop()

        dfs(0, 0)

        return ans