class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]

        return ''.join(strs)

    def decode(self, s: str) -> List[str]:

        ans = []

        i = 0
        while i < len(s):

            temp = []
            j = i

            while s[j].isnumeric():
                temp.append(s[j])
                j += 1

            if temp:
                temp = int(''.join(temp))
                j += 1
                ans.append(s[j: j + temp])

            
                i = j + temp
    
            

            

        return ans
        

