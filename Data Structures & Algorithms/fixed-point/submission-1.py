class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        smaller=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==mid:
                smaller=mid
                r=mid-1
            elif arr[mid]<mid:
                l=mid+1
            else:
                r=mid-1
        return smaller

