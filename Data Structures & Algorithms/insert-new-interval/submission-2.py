class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        
        res=[]
        curStart=newInterval[0]
        done=0
        for i in range(len(intervals)):
            if intervals[i][0]<curStart:
                res.append(intervals[i])
                continue
            if curStart<intervals[i][0]:
                if not done:
                    res.append(newInterval)
                    done=1
                res.append(intervals[i])
        if not done:
            res.append(newInterval)
        # print(res)
        #Now merge them 
        
        output=[res[0]]
        for start,end in res[1:]:
            lastEnd=output[-1][1]
            if lastEnd>=start:
                output[-1][1]=max(end,lastEnd)
            else:
                output.append([start,end])
            # ans.append([start,end])
        return output
            
        