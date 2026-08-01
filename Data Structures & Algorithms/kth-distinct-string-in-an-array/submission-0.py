from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=defaultdict(int)
        for x in arr:
            d[x]+=1
        for string in arr:
            if d[string]==1:
                k-=1
                if k==0:
                    return string
            
        if k>0:
            return ""