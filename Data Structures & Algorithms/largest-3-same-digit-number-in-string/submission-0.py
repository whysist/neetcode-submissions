class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        currMax=None
        for i in range(n-2):
            subs=num[i:i+3]
            s=set(subs)
            if currMax==None and len(s)==1:
                currMax=int(subs)
            elif len(s)>1 or int(subs)<=currMax:
                continue 
            else:
                currMax=int(subs)
        if currMax==0:
            return "000"
        return str(currMax) if currMax is not None else ""

        