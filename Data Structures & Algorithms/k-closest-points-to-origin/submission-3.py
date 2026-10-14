from heapq import heapify,heappush,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points)==1 and k>0:
            return points
        
        heap=[]
        for cordinates in points:
            x=cordinates[0]
            y=cordinates[1]
            d=math.sqrt(x**2 + y**2)
            heappush(heap,(-d,(x,y)))
            if len(heap)>k:
                heappop(heap)
        res=[]
        for dis,cord in heap:
            res.append([cord[0],cord[1]])
        return res
        # print(heap)



