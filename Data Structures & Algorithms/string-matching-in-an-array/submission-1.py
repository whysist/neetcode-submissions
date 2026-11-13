class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for word in words:
            # c=0
            for i in range(len(words)):
                if words[i]!=word and words[i].find(word)!=-1:
                    res.append(word)
                    break
        return res