class Solution:
    def maxScore(self, s: str) -> int:
        if len(s)==1:
            return 1
        if len(set(s))==1:
            return len(s)-1
        ans=0
        pre=[0]*len(s)
        n=len(s)
        suf=[0]*len(s)
        pre[0]=1 if s[0]=='0' else 0
        suf[n-1]=1 if s[n-1]=='1' else 0
        for i in range(1,n):
            if s[i]=='0':
                pre[i]=pre[i-1]+1
            else:
                pre[i]=pre[i-1]
        for i in range(n-2,-1,-1):
            if s[i]=='1':
                suf[i]=suf[i+1]+1
            else:
                suf[i]=suf[i+1]
        # print(pre)
        # print(suf)
        for i in range(1,n):
            if pre[i]+suf[i]>ans:
                ans=pre[i-1]+suf[i]
        return ans