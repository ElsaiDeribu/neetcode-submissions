class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        st = []

        for idx, num in enumerate(temperatures):

            while st and temperatures[st[-1]] < num:
                i = st.pop()
                result[i] = idx - i

            st.append(idx)


        return result
