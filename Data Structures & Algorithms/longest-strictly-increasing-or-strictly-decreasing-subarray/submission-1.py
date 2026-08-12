class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        inc,dec=1,1
        max_inc,max_dec=1,1
        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dec=1
                inc+=1
                max_inc=max(max_inc,inc)
            elif nums[i]<nums[i-1]:
                inc=1
                dec+=1
                max_dec=max(max_dec,dec)
            else:
                inc=1
                dec=1
                
             
        # for i in range(1,len(nums)):
        #     if nums[i]>nums[i-1]:
        #         inc+=1
        #     else:
        #         inc=1
        # for i in range(1,len(nums)):
        #     else:
        #         dec=1
        return max(max_inc,max_dec)

        