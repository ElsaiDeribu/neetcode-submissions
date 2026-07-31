class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_freq = defaultdict(int)
        
        l = 0
        ans = 0

        for r in range(len(s)):

            window_freq[s[r]] += 1

            while window_freq[s[r]] > 1:
                window_freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans


            

        