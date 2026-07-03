from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0
        d=defaultdict(int)
        for x in arr:
            d[x]+=1
        ans=0
        for num in arr:
            if num+1 in d:
                ans+=1
                d[num+1]-=1
        return ans
        