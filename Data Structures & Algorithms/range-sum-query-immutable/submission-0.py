class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=nums
        self.pre=[]
        self.pre.append(nums[0])
        for i in range(1,len(nums)):
            self.pre.append(self.pre[i-1]+nums[i])
        print(self.pre)
        

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.pre[right]-self.pre[left-1]
        else:
            return self.pre[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)