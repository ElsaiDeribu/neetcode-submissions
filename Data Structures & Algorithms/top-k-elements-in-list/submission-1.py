class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        freq_grouped_nums = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            freq_grouped_nums[freq].append(num)

        ans = []

        for i in range(len(freq_grouped_nums) - 1, -1, -1):
            
            for num in freq_grouped_nums[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans


        