class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        freq_sorted_nums = sorted(count.items(), key = lambda x: -x[1])[:k]

        return [key for key, val in freq_sorted_nums]
        