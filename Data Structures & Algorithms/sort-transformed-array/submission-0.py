class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def func(x,a,b,c):
            return (a*(x**2) + b*x +c)
        res=[]
        for num in nums:
            res.append(func(num,a,b,c))
        res.sort()
        return res