class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s)==1 :
            return -1
        if len(s)==2 and s[0]==s[1]:
            return 0
            
        ans=-1
        chs=set(s)
        occur=[(s.find(ch),s.rfind(ch)) for ch in chs]
        # print(occur)
        for first,last in occur:
            ans=max(ans,last-first-1)
        return ans
        