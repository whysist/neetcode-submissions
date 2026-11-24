class MovingAverage:

    def __init__(self, size: int):
        self.stream=[]
        self.size=size

    def next(self, val: int) -> float:
        self.stream.append(val)

        window=len(self.stream) if len(self.stream)<self.size else self.size
        n=len(self.stream)
        curSum=0
        for i in range(n-1,n-window-1,-1):
            curSum+=self.stream[i]
        return curSum/window


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
