class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]

        return ''.join(strs)

    def decode(self, s: str) -> List[str]:

        ans = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            j += 1

            ans.append(s[j: j + length])
            
            i = j + length
    

        return ans
        

