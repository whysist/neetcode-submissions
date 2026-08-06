import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]
        for num in count:
            freq=count[num]
            heapq.heappush(heap,(freq,num))
            # print(heap)
            if len(heap)>k:
                heapq.heappop(heap)
        # print(heap)
        res=[]
        for c,num in heap:
            res.append(num)
        return res
        