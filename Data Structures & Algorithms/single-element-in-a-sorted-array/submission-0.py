class Solution:
    def singleNonDuplicate(self, nums: List[int]) ->int:
        ans=-1
        if len(nums)==1:
            return nums[0]
            
        def binSearch(l,r):
            nonlocal ans
            if l>r:
                return False
            m=(l+r)//2
            if m>0 and m<len(nums)-1: 
                if nums[m-1]<nums[m]<nums[m+1]:
                    ans=nums[m]
                    return True
            left=binSearch(l,m-1)
            right=binSearch(m+1,r)
            return left or right or False
        
        binSearch(0,len(nums)-1)
        if ans==-1:
            if nums[0]!=nums[1]:
                return nums[0]
            if nums[len(nums)-1]!=nums[len(nums)-2]:
                return nums[len(nums)-1]
        return ans

        