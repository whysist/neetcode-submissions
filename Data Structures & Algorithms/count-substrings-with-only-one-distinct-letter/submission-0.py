class Solution:
    def countLetters(self, s: str) -> int:
        if len(s)==1:
            return 1
        
        ans=0
        def numSubs(n):
            return ((n*(n+1))//2)
        l,r=0,0
        n=len(s)
        while r<n:
            while r<n and s[r]==s[l]:
                r+=1
            ans+=numSubs(r-l)
            # print(ans,r,l)
            l=r
        return ans