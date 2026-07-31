class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res = sorted(list(zip(position, speed)))
        for idx, (pos, s) in enumerate(res):
            time = (target - pos) / s
            res[idx] = time
        
        st = []
        for time in res:
            while st and st[-1] <= time:
                st.pop()
            st.append(time)



        return len(st)