class Solution:
    def minChanges(self, s: str) -> int:
        ans=0
        n=len(s)
        for i in range(0,n-1,2):
            subs=s[i:i+2]
            ans+=(1 if subs[0]!=subs[1] else 0)
            # print(subs,ans)
        return ans
