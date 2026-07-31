class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        want = Counter(s1)
        have = defaultdict(int)
        matches = 0
        required = len(want)
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            have[c] += 1
            if c in want and have[c] == want[c]:
                matches += 1
            elif c in want and have[c] == want[c] + 1:
                # was matching, now overshot
                matches -= 1

            if r - l + 1 > len(s1):
                left_c = s2[l]
                if left_c in want and have[left_c] == want[left_c]:
                    matches -= 1
                elif left_c in want and have[left_c] == want[left_c] + 1:
                    matches += 1
                have[left_c] -= 1
                l += 1

            if matches == required:
                return True

        return False



        