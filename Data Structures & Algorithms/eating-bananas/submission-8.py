class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)
        
        def calcTime(k):
            ans=0
            for pile in piles:
                ans+= math.ceil(pile/k)
            return ans

        l=1
        total=sum(piles)
        r=max(piles)
        while l<r:
            mid=(l+r)//2
        
            hours=calcTime(mid)
            # print(f'k:{mid},hours:{hours}')

            if hours<=h:
                r=mid
            else:
                l=mid+1
        return r

        