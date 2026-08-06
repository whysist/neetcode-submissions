class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "[EMPTY_LIST]"

        res=""
        for word in strs:
            res+= str(len(word))+":"+word
        return res

    def decode(self, s: str) -> List[str]:
        if s=="[EMPTY_LIST]":
            return []
        if s=="":
            return [""]

        i=0
        res=[]
        while i<len(s):
            j=i
            while s[j]!=":":
                j+=1
            length=int(s[i:j])
            start=j+1
            end=j+length+1
            res.append(s[start:end])
            i=end
        return res


        


