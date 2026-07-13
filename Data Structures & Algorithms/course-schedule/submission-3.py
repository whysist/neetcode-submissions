from collections import deque
class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        inDeg=[0]*(numCourses)
        for u,v in pre:
            adj[v].append(u)
            inDeg[u]+=1
        q=deque()
        for i in range(numCourses):
            if inDeg[i]==0:
                q.append(i)
        finish=0
        while q:
            course=q.popleft()
            finish+=1
            for neigh in adj[course]:
                inDeg[neigh]-=1
                if inDeg[neigh]==0:
                    q.append(neigh)
        return finish==numCourses
