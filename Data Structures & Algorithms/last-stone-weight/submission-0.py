class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        print(stones)
        while len(stones) > 1 :
            a = - heapq.heappop(stones)
            b = - heapq.heappop(stones)

            if a>b:
                remaining = (b-a)
                heapq.heappush(stones,remaining)
        if len(stones) ==1:
            return - stones[0]
        
        else:
            return 0




        