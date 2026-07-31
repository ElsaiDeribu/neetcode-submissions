class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []
        comb = []

        def recur(start, remainder):

            if remainder < 0:
                return

            if remainder == 0:
                ans.append(comb.copy())
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                comb.append(candidates[i])
                recur(i + 1, remainder - candidates[i])
                comb.pop()


        recur(0, target)

        return ans



        