from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==1:
            return 1
        n=len(s)
        ans=0
        check=[0]*26
        L=0
        # check[ord(s[0])]+=1
        for R in range(n):
            check[ord(s[R])-ord('A')]+=1
            # print(R)
            maxCount=0
            for count in check:
                if count>maxCount:
                    maxCount=count
            while (R-L+1)-maxCount > k:
                check[ord(s[L])-ord('A')]-=1
                L+=1
            windowLen=R-L+1
            ans=max(ans,windowLen)
            
        return ans
                
                

        