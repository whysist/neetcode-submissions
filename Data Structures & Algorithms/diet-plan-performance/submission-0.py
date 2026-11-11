class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans=0
        n=len(calories)
        for i in range(n-k+1):
            sub=calories[i:i+k]
            currSum=sum(sub)
            if currSum>upper:
                ans+=1
            elif currSum<lower:
                ans-=1
        return ans


