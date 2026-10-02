import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        net=[[float('inf')]*(n) for _ in range(n)]
        adj=[[] for _ in range(n)]
        for u,v,t in times:
            adj[u-1].append((v-1,t))
        src=k-1
        dist=[float('inf')]*n
        # from src to all other nodes. 
        # the farthest distance wins
        # if farthest distance != float('inf')/-1 its valid else it's invalid
        
        dist[src]=0
        heap=[]
        heapq.heappush(heap,(0,src))
        while heap:
            curtime,node=heapq.heappop(heap)
            if curtime!=dist[node]:
                continue
            for neigb,dt in adj[node]:
                time=curtime+dt
                if time<dist[neigb]:
                    dist[neigb]=time
                    heapq.heappush(heap,(time,neigb))
        # ans=0
        return max(dist) if max(dist)!=float('inf') else -1
