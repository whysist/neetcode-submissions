class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        print(l)
        res=[]
        for word in l:
            res.append(word[::-1])
        return " ".join(res)


