class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==1:
            return heights[0]
        max_area=0
        n=len(heights)+1
        stack=[]
        for i,h in enumerate(heights+[0]):
            while stack and heights[stack[-1]]>h:
                height=heights[stack.pop()]
                l=stack[-1] if stack else -1
                w=i-l-1
                max_area=max(max_area,height*w)
            stack.append(i)
        return max_area