class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes=0
        curr=0
        for x in nums:
            if x==1:
                curr+=1
            else:
                curr=0
            maxOnes=max(curr,maxOnes)
        return maxOnes
        