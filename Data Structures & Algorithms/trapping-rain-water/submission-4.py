class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        n=len(height)
        ans=0
        stack=[]
        for i,h in enumerate(height):
            while stack and h>=height[stack[-1]]:
                idx=stack.pop()
                if not stack:
                    break 
                
                w=i-stack[-1]-1
                ht=min(height[stack[-1]],h)-height[idx]
                ans+=(ht*w)
            stack.append(i)
            # print(ans,stack)
        return ans

            

        