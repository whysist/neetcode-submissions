class Solution:
    def arrangeCoins(self, n: int) -> int:
        cum=0
        ans=0
        for i in range(1,n+1):
            cum+=i
            if cum>n:
                break
            ans+=1
        return ans
        