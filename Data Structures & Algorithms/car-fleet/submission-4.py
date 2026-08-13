class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=sorted(zip(position,speed))
        n=len(position)
        stack=[]
        fleets=0
        def timeTaken(p,s):
            return (target-p)/s
        # print(arr)
        for i in range(n-1,-1,-1):
            if stack and timeTaken(stack[-1][0],stack[-1][1])>=timeTaken(arr[i][0],arr[i][1]):
                continue
            stack.append(arr[i])
            fleets+=1
        return fleets