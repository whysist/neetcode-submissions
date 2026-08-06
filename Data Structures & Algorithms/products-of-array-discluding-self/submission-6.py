class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_pro=[1]*(n)
        right_pro=[1]*(n)
        left_pro[0]=nums[0]
        right_pro[n-1]=nums[n-1]
        for i in range(1,n):
            left_pro[i]=nums[i]*left_pro[i-1]
        for i in range(n-2,-1,-1):
            right_pro[i]=nums[i]*right_pro[i+1]
        ans=[0]*(n)
        ans[0]=right_pro[1]
        ans[n-1]=left_pro[n-2]
        for i in range(1,n-1):
            ans[i]=left_pro[i-1]*right_pro[i+1]
        return ans

        