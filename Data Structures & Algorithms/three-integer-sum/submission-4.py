class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()
        for i in range(n-1):
            target= -nums[i]
            L=i+1
            R=n-1
            while L<R:
                if nums[L]+nums[R]==target:
                    res.add((nums[i],nums[L],nums[R]))
                    L+=1
                    R-=1
                elif nums[L]+nums[R]<target:
                    L+=1
                else:
                    R-=1
        print(res)
        return list(res)
            
        