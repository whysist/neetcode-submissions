class Solution:
    def isDecomposable(self, s: str) -> bool:
        if len(s)<2:
            return False

        n=len(s)
        pairs=0
        i=0
        while i<n:
            j=i+1
            while j<n and s[j]==s[i]:
                j+=1
            rem=(j-i)%3
            if rem==1:
                return False
            if rem==2:
                pairs+=1
            i=j
        return pairs==1


