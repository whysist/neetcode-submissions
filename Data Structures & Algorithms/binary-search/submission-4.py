class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                break
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans
                