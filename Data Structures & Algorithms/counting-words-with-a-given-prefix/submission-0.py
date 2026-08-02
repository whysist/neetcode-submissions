class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(pref)
        c=0
        for word in words:
            if len(word)<n:
                continue
            if word[:n]==pref:
                c+=1
        return c

        