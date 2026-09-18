class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s)==1:
            return 0
        ans=0
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
            elif len(stack)>0 and ch==")":
                ans=max(ans,len(stack))
                stack.pop()
        return ans
                

        