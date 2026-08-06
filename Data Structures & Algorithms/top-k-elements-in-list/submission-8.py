import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        # print(buckets)
        for num in count:
            freq=count[num]
            buckets[freq].append(num)
        count=k
        res=[]
        # print(buckets)
        for i in range(len(buckets)-1,0,-1):
            res.extend(buckets[i])
            if len(res)==k:
                return res
            
            

        