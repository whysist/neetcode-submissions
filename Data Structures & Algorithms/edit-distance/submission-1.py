class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        memo={}
        def dfs(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                memo[(i,j)]=dfs(i+1,j+1)
                return memo[(i,j)]
            
            ins=memo[(i+1,j)] if (i+1,j) in memo else dfs(i+1,j)
            dele=memo[(i,j+1)] if (i,j+1) in memo else dfs(i,j+1)
            rep=memo[(i+1,j+1)] if (i+1,j+1) in memo else dfs(i+1,j+1)
            res=min(ins,dele) #compare insertion and deletion
            memo[(i,j)]=min(res,rep) +1 #compare res with replacement and counts current op too
            return memo[(i,j)]
        return dfs(0,0)


        