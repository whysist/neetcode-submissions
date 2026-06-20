class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        check=set()
        ans=float('-inf')
        L=0
        R=-1
        while R<len(s)-1:
            if s[R+1] not in check:
                R+=1
                check.add(s[R])
                ans=max(ans,R-L+1)
            else:
                while s[R+1] in check:
                    check.remove(s[L])
                    L+=1
        return ans