class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)


        def count(word):
            
            chrs = [0] * 26

            for c in word:
                chrs[ord(c) - 97] += 1

            return chrs



        for word in strs:
            srtd_wrd = count(word)
            group[str(srtd_wrd)].append(word)

        ans = [val for key, val in group.items()]

        return ans

