class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)

        def back(i,subs):
            if i==n:
                res.append(subs[:])
                return 
            
            subs.append(nums[i])
            back(i+1,subs)
            subs.pop()
            back(i+1,subs)
        
        back(0,[])
        return res
