class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        want = Counter(s1)
        have = defaultdict(int)
        l = 0


        for r in range(len(s2)):

            have[s2[r]] += 1

            while r - l + 1 > len(s1):

                have[s2[l]] -= 1
                if have[s2[l]] == 0: have.pop(s2[l])
                l += 1

            if have == want:
                return True



        return False
        