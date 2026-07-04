class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check=[0]*26
        for ch in ransomNote:
            check[ord(ch)-ord('a')]+=1
        for ch in magazine:
            check[ord(ch)-ord('a')]-=1
        
        for i in check:
            if i>0:
                return False
        return True