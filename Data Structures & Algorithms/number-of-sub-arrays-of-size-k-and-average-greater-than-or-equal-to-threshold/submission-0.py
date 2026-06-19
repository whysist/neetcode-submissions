class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr)==1:
            return 1 if nums[0]>threshold else 0
        
        L=0
        c=0
        currSum=0
        for i in range(k):
            currSum+=arr[i]
        if (currSum/k)>=threshold:
            c+=1
        print(currSum/k)
        for R in range(k,len(arr)):
            currSum-=arr[L]
            currSum+=arr[R]
            print(currSum/k)
            if (currSum/k)>=threshold:
                c+=1
            L+=1
        return c
             