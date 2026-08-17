class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(l,r):
            if l>r:
                return -1
            mid=(l+r)//2
            if nums[mid]>target:
                return binSearch(l,mid-1)
            elif nums[mid]<target:
                return binSearch(mid+1,r)
            else:
                return mid
        return binSearch(0,len(nums)-1)        