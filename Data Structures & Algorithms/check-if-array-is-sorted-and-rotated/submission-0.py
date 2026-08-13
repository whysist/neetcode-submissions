class Solution:
    def check(self, nums: List[int]) -> bool:
        len1=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]<=nums[i+1]:
                len1+=1
            else:
                break
        if len1==n-1:
            return True
        for j in range(len1+1,n-1):
            if nums[j]<=nums[j+1]:
                continue
            else:
                return False
        return nums[-1]<=nums[0]