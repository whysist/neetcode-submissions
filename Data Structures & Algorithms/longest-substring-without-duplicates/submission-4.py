class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        check=set()
        ans=float('-inf')
        L=0
        R=0
        while R<len(s):
            while s[R] in check:
                check.remove(s[L])
                L+=1
            check.add(s[R])
            R+=1
            ans=max(ans,R-L)
        return ans
