class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        fmap=[0]*26
        for ch in s:
            fmap[ord(ch)-ord('a')]+=1
        for ch in t:
            fmap[ord(ch)-ord('a')]-=1
        return fmap==([0]*26)
        
        