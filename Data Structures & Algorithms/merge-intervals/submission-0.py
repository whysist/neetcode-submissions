class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        res=[]
        intervals.sort()
        l=[intervals[0]]
        for start,end in intervals:
            lastEnd=l[-1][1]
            if start<=lastEnd:
                l[-1][1]=max(lastEnd,end)
            else:
                l.append([start,end])
        return l

        