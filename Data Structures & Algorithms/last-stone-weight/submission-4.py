import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            heaviest=0-heapq.heappop(heap)
            second_heaviest=0-heapq.heappop(heap)
            heapq.heappush(heap,0-(heaviest-second_heaviest))
        return 0-(heapq.heappop(heap))

        

