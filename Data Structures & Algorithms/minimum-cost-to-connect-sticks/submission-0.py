from heapq import heappush,heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks)==1:
            return 0
        heap=sorted(sticks)
        # print(heap)
        ans=0
        while len(heap)>1:
            # print(f'heap:{heap}')
            u=heappop(heap)
            v=heappop(heap)
            cost=u+v
            ans+=cost
            # print(u,v,cost)
            heappush(heap,cost)
        # print(heap)
        
        return ans

