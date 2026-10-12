class Solution:
    def singleNonDuplicate(self, nums: List[int]) ->int:
        ans=-1
        if len(nums)==1:
            return nums[0]
        # Every pair before the single element starts at even index i.e 0,2,4 etc 
        # Every pair after the single elemennt starts at odd index    
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if m%2==1:
                m-=1 #make m start at even indx
            if nums[m]==nums[m+1]: # if pair starts at even and ends at odd,
                l=m+2
            else:
                r=m
        return nums[l]
            

        