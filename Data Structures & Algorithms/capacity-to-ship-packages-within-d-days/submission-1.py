class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days==1:
            return sum(weights)
        if days==len(weights):
            return max(weights)
        # find out whether this capacity is enough to ship it in <=days
        def canShip(cap):
            currWeight=0
            req_days=1
            for w in weights:
                if currWeight+w>cap:
                    req_days+=1
                    currWeight=w
                else:
                    currWeight+=w
            return req_days<=days
        l=max(weights)
        r=sum(weights)

        while l<r:
            mid=(l+r)//2
            d=sum(weights)//mid #capacity through binary search

            if canShip(mid):
                r=mid

            else:
                l=mid+1
        return r