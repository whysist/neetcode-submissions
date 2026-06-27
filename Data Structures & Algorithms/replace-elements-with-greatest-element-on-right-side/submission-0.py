class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            arr[0]=-1
            return arr
        n=len(arr)
        curr=arr[n-1]
        arr[n-1]=-1
        for i in range(n-2,-1,-1):
            if arr[i]>curr:
                temp=arr[i]
                arr[i]=curr
                curr=temp
            else:
                arr[i]=curr
        return arr