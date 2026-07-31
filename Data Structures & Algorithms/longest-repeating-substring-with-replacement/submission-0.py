class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        upper_chrs = [chr(aski) for aski in range(65, 65 + 26)]
        ans = 0

        for letter in upper_chrs:

            flip = k

            longest = 0
            l = 0

            for r in range(len(s)):

                if s[r] != letter:
                    flip -= 1

                while flip < 0:
                    if s[l] != letter:
                        flip += 1
                    l += 1

                longest = max(longest, r - l + 1)

            ans = max(ans, longest)



        return ans