class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        total=sum(nums)
        S=total//2
        n=len(nums)
        dp=[[False]*(S+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        
        for i in range(1,n+1):
            for j in range(1,S+1):
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[n][S]
