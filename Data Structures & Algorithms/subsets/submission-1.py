class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [[],[nums[0]]]
        res=[]
        def back(i,subs):
            if i==len(nums):
                res.append(subs[:])
                return 
            subs.append(nums[i])
            back(i+1,subs)
            subs.pop()
            back(i+1,subs)
        back(0,[])
        return res