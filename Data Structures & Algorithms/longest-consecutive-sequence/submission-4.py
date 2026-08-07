class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        check=set(nums)
        # print(check)
        for i in range(n):
            if (nums[i]-1) not in check:
                length=1
                while (nums[i]+length) in check:
                    length+=1
                ans=max(length,ans)
        return ans