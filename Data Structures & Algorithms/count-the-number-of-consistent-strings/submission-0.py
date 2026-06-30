class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check=set(allowed)
        ans=0
        for word in words:
            s=set(word)
            b=0
            for ch in s:
                if ch not in check:
                    b=1
                    break
            if not b: ans+=1
            del s
        return ans

            
        