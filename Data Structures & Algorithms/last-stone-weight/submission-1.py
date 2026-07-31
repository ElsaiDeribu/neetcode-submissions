class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        # TC: O(nlogn)
        # SC: O(n)
        for idx, val in enumerate(stones):
            stones[idx] = -val


        heapq.heapify(stones)

        while len(stones) > 1:
            large = -heapq.heappop(stones)
            small = -heapq.heappop(stones)

            if large != small:
                heapq.heappush(stones, -(large - small))

        if len(stones) == 1:
            return -stones[0]

        return 0