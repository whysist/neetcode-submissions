class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        arr.sort()
        if arr[0]!=1:
            arr[0]=1
        # print(arr)

        for i in range(1,len(arr)):
            if arr[i]==1:
                continue
            
            arr[i]=min(arr[i-1]+1,arr[i])
        return arr[-1]
